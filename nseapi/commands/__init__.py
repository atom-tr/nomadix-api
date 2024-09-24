from . import radius as _radius
from . import subscriber as _subscriber
from nseapi.types import Command, MACAddress

__all__ = ['Radius', 'Subscriber', 'CACHE_UPDATE']


CACHE_UPDATE = lambda *args, **kwargs: Command('CACHE_UPDATE', {
    'attributes': {
        'MAC_ADDR': {'type': MACAddress, 'required': True},
    }
}, *args, **kwargs)
"""
The memory authorization table entry specified 
by the MAC address will have its status changed from "pending" to "authorized". 
NOTE: It is important to update the cache to enable proper access for the subscribe

Kwargs:
    - mac_addr: Subscriber's MAC address
"""

class Radius:
    LOGIN = lambda *args, **kwargs: Command(*_radius.LOGIN, *args, **kwargs)
    """
    The Portal Page web server can send this command to instruct the NSE to send a RADIUS 
    authentication request to the RADIUS server to authenticate a subscriber

    Kwargs:
        - SUB_USER_NAME: Subscriber's username (char [96]) 
        - SUB_PASSWORD: Subscriber's password (char [128])  
        - SUB_MAC_ADDR: Subscriber's MAC address (char [12])  
        - PORTAL_SUB_ID (optional): 
            Unique identifier that the Portal Page web server can send to the 
            NSE which will be sent back with status response (char [36])
    """

    LOGOUT = lambda *args, **kwargs: Command(*_radius.LOGOUT, *args, **kwargs)
    """
    The Portal Page web server can send this command to 
    instruct the NSE to logout the subscriber.
    
    Kwargs:
        - SUB_USER_NAME: Subscriber's username (char [96]) 
        - SUB_MAC_ADDR: Subscriber's MAC address (char [12])  
    """

class Subscriber:
    ADD_USER = lambda *args, **kwargs: Command(*_subscriber.SUBSCRIBER_ADD, *args, **kwargs)
    ADD_DEVICE = lambda *args, **kwargs: Command(*_subscriber.DEVICE_ADD, *args, **kwargs)
    """
    In which a specified Device is authorized for access, 
    and is added to the NSE authorized MAC address database. 
    The device is furthermore guaranteed access at any time by reserving a 
    permanent entry for it in the NSE Current (active) subscriber table
    
    Kwargs:
        - MAC_ADDR (MACAddress, required)
        - BANDWIDTH_MAX_DOWN: Maximum Downstream bandwidth (int, optional)
        - BANDWIDTH_MAX_UP (int, optional): Maximum Upstream bandwidth 
        - CLASS_NAME: (char[64], optional). 
            Indicates the class that traffic to/from this user should be assigned to for Class-Based Queuing purposes
        - DHCP_SUBNET: DHCP subnet (char[10], optional). 
            Subnet based on configured DHCP subnets in the NSE
        - QOS_POLICY: QoS Policy (str, optional). 
            Select and add the QoS Policy that is configured on the NSE to the profile for the user
        - SMTP_REDIRECT: SMTP Redirection (bool, optional). Default: True
        - USER_DEF1: User definable string (char[128], optional). Default: empty
        - USER_DEF2: User definable string (char[128], optional). Default: empty
        - DEVICE_NAME: A short name for the device (char[96])
        - IP6_ADDR: The IPv6 address associated with the device, if any. 
        - IP_ADDR: The IP address associated with the device, if any.
        - PROXY_ARP: Enable (TRUE) or disable (FALSE) Proxied ARP for this device.
        - VLAN: 802.1Q VLAN port that device is attached to (0 ≤ VLAN ≤ 4095). 
            If omitted or zero, the device will be granted access no matter where it has attached; 
            but if a non-zero VLAN is specified, the device will only be granted access when attached to that VLAN.
    """

    ADD_GROUP = lambda *args, **kwargs: Command(*_subscriber.GROUP_ADD, *args, **kwargs)
    ADD_ACCESS_CODE = lambda *args, **kwargs: Command(*_subscriber.ACCESS_CODE_ADD, *args, **kwargs)

    SET_BANDWIDTH_UP = lambda *args, **kwargs: Command(*_subscriber.SET_BANDWIDTH_UP, *args, **kwargs)
    """Set the Bandwidth Up for an authorized subscriber.

    Kwargs:
        - mac_addr: Subscriber's MAC address
        - bandwidth_up: Number measured in Kbps 
          (i.e. for 128,000 bits per second, enter 128)
    """
