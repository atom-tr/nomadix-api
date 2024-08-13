import sys
import logging
import socket
import datetime
import time
import urllib
import urllib.request
import xmltodict

import nseapi.exceptions as nse_err

logger = logging.getLogger(__name__)

class Device:
    
    def __init__(self, *args, **kwargs):
        # ----------------------------------------
        # setup instance connection/open variables
        # ----------------------------------------
        self._hostname = args[0] if len(args) else kwargs.get("host")
        if not self._hostname:
            raise ValueError("You must provide 'host' value")
        self._port = kwargs.get("port", 1111)
        self._conn_open_timeout = kwargs.get("conn_open_timeout", 30)
        self._auth_user = kwargs.get("user")  or kwargs.get("usr")
        self._auth_password = kwargs.get("password") or kwargs.get("passwd")

        # initialize instance variables
        self._conn = None
        # public attributes
        self.connected = False
    
    @property
    def connected(self):
        return self._connected
    
    _auto_probe = 0  # default is no auto-probe


    @property
    def hostname(self):
        """
        :returns: the host-name of the NSE device.
        """
        return (
            self._hostname
            if (self._hostname != "localhost")
            else self.facts.get("hostname")
        )
    
    @property
    def port(self):
        """
        :returns: the port (str) to connect to the NSE device
        """
        return self._port
    
    @property
    def timeout(self):
        """
        :returns: the current RPC timeout value (int) in seconds.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        """
        Used to change the RPC timeout value (default=30 sec).

        :param int value:
            New timeout value in seconds
        """
        try:
            self._timeout = int(value)
        except (ValueError, TypeError):
            raise RuntimeError(
                "could not convert timeout value of %s to an " "integer" % (value)
            )

    @property
    def user(self):
        """
        :returns: the login user (str) accessing the NSE device
        """
        return self._auth_user


    @property
    def password(self):
        """
        :returns: ``None`` - do not provide the password
        """
        return None  # read-only

    @password.setter
    def password(self, value):
        """
        Change the authentication password value.  This is handy in case
        the calling program needs to attempt different passwords.
        """
        self._auth_password = value

    @connected.setter
    def connected(self, value):
        if value in [True, False]:
            self._connected = value
    
    def probe(self, timeout=5, intvtimeout=1):
        """
        Probe the device to determine if the Device can accept a remote
        connection.
        This method is meant to be called *prior* to :open():

        :param int timeout:
          The probe will report ``True``/``False`` if the device report
          connectivity within this timeout (seconds)

        :param int intvtimeout:
          Timeout interval on the socket connection. Generally you should not
          change this value, but you can if you want to twiddle the frequency
          of the socket attempts on the connection

        :returns: ``True`` if probe is successful, ``False`` otherwise
        """
        start = datetime.datetime.now()
        end = start + datetime.timedelta(seconds=timeout)
        probe_ok = True

        while datetime.datetime.now() < end:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(intvtimeout)
            try:
                s.connect((self.hostname, int(self._port)))
                s.shutdown(socket.SHUT_RDWR)
                s.close()
                break
            except:
                time.sleep(1)
                pass
        else:
            probe_ok = False

        return probe_ok

    def open(self, *args, **kwargs):
        """
        Opens a connection to the device using existing login/auth
        information.
        """
        pass
        auto_probe = kwargs.get("auto_probe", self._auto_probe)
        if auto_probe:
            if not self.probe(auto_probe):
                raise nse_err.ProbeError(self)
        
        url = f"http://{ self.hostname }:{ str(self._port) }/usg/command.xml"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self._req = urllib.request.Request(url, headers=headers, method="POST")
        self.connected = True
        return self


    def close(self):
        """
        Closes the connection to the device only if connected.
        """
        if self.connected is True:
            self.connected = False
    
    
    def __repr__(self):
        return "NSE(%s)" % self.hostname
    
    def execute(self, xml, ignore_warning=False, **kwargs):
        encode = None if sys.version < "3" else "unicode"
        self._req.data = xml.encode(encode)
        try:
            with urllib.request.urlopen(self._req, timeout=self.timeout) as rsp:
                _rsp = rsp.read().decode(encode)
                try:
                    _data = xmltodict.parse(_rsp)
                except xmltodict.expat.ExpatError:
                    raise nse_err.ParseError(self, _rsp)
                else:
                    data = _data.get('USG')
                    if data['@RESULT'] == 'ERROR':
                        raise nse_err.USGError('Execute request failed', data)
                    return data
        except Exception as e:
            raise nse_err.ConnectError(self, e)

    # -----------------------------------------------------------------------
    # Context Manager
    # -----------------------------------------------------------------------

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connected:
            try:
                self.close()
            except Exception as ex:
                # exit should not raise any exception
                logger.error("Close in context manager hit exception: {}".format(ex))
        