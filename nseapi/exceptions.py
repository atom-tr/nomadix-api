class USGError(Exception):
    """Base class for USG-related errors."""

    def __init__(self, message, rsp):
        super().__init__(message)
        self._error_num = int(rsp.get("ERROR_NUM"))
        self._error_desc = rsp.get("ERROR_DESC") or self.get_error_description()

    @property
    def error_desc(self):
        return self._error_desc

    def __str__(self):
        return f"{self.args[0]}: {self.error_desc} (Error No. {self._error_num})"

    def __repr__(self) -> str:
        return f"<USGError {self._error_num}: {self.error_desc}>"

    def get_error_description(self):
        error_descriptions = {
            100: "Parsing error",
            101: "Unrecognized command",
            102: "Required attribute is missing",
            103: "Required data is missing",
            200: "Unknown room number",
            201: "Unknown user name",
            202: "Unknown user MAC address",
            203: "Wrong password",
            204: "User name already used",
            205: "Too many subscribers",
            206: "Unable to provide all requested data",
            207: "AAA internal error (when AAA is not configured correctly for the command request)",
            208: "Wrong Plan Number",
            209: "User is already valid",
            210: "Specified valid-until time is invalid",
            211: "Specified DHCP subnet does not exist",
            300: "User RADIUS account not found",
            301: "User RADIUS authorization denied",
            302: "User PMS authorization denied",
            303: "Unsupported payment method",
            304: "MAC Address does not belong to room location",
        }
        return error_descriptions.get(self._error_num, "Unknown error")


class ConnectError(Exception):
    """
    Parent class for all connection related exceptions
    """

    def __init__(self, dev, msg=None):
        self.dev = dev
        self._orig = msg

    @property
    def user(self):
        """login user-name"""
        return self.dev.user

    @property
    def host(self):
        """login host name/ipaddr"""
        return self.dev.hostname

    @property
    def port(self):
        """login XML port"""
        return self.dev._port

    @property
    def msg(self):
        """login XML port"""
        return self._orig

    def __repr__(self):
        if self._orig:
            return "{}(host: {}, msg: {})".format(
                self.__class__.__name__, self.dev.hostname, self._orig
            )
        else:
            return "{}({})".format(self.__class__.__name__, self.dev.hostname)

    __str__ = __repr__


class ProbeError(ConnectError):
    """
    Generated if auto_probe is enabled and the probe action fails
    """


class ConnectAuthError(ConnectError):
    """
    Generated if the user-name, password is invalid
    """


class ConnectTimeoutError(ConnectError):
    """
    Generated if the NETCONF session fails to connect, could
    be due to the fact the device is not ip reachable; bad
    ipaddr or just due to routing
    """


class ConnectUnknownHostError(ConnectError):
    """
    Generated if the specific hostname does not DNS resolve
    """


class ConnectRefusedError(ConnectError):
    """
    Generated if the specified host denies the NETCONF; could
    be that the services is not enabled, or the host has
    too many connections already.
    """
