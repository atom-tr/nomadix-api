from nseapi.types import MACAddress, BaseCommand
from nseapi.commands.options import subscriber as spec

__all__ = ["ADD_USER", "ADD_DEVICE", "ADD_GROUP", "ADD_ACCESS_CODE"]


class ADD_USER(BaseCommand):
    """
    Authorizes a subscriber for access and adds them to the NSE's MAC authorization table.
    If the subscriber is in the 'Current' memory table,
    the Update Cache XML command must follow to correctly update the subscriber.

    Kwargs:
        - MAC_ADDR (MACAddress, required)
        - BANDWIDTH_MAX_DOWN (int, optional): Maximum Downstream bandwidth
        - BANDWIDTH_MAX_UP (int, optional): Maximum Upstream bandwidth
        - CLASS_NAME (char[64], optional): Class for Class-Based Queuing
        - DHCP_SUBNET (char[10], optional): DHCP subnet
        - QOS_POLICY (str, optional): QoS Policy
        - SMTP_REDIRECT (bool, optional): SMTP Redirection. Default: True
        - USER_DEF1 (char[128], optional): User definable string. Default: empty
        - USER_DEF2 (char[128], optional): User definable string. Default: empty
        - DEVICE_NAME (char[96]): Device name
        - IP6_ADDR (optional): IPv6 address
        - IP_ADDR (optional): IP address
        - PROXY_ARP (optional): Enable/Disable Proxied ARP
        - VLAN (0 ≤ VLAN ≤ 4095, optional): 802.1Q VLAN port.
        If omitted or zero, access is granted regardless of attachment;
        otherwise, access is granted only when attached to the specified VLAN.
    """

    _type, _spec, *_ = spec.SUBSCRIBER_ADD

    def __init__(self, mac_addr: MACAddress, *args, **kwargs):
        self._transform(MAC_ADDR=mac_addr, *args, **kwargs)


class ADD_DEVICE(BaseCommand):
    """
    Authorizes a device for access and adds it to the NSE's authorized MAC address database, ensuring permanent access.

    Kwargs:
        - MAC_ADDR (MACAddress, required)
        - BANDWIDTH_MAX_DOWN (int, optional): Maximum Downstream bandwidth
        - BANDWIDTH_MAX_UP (int, optional): Maximum Upstream bandwidth
        - DEVICE_NAME (char[96], required): Device name
    For a complete list of available kwargs options,
    refer to the ADD_DEVICE method's documentation by running ADD_DEVICE.help().
    """

    _type, _spec, *_ = spec.DEVICE_ADD

    def __init__(self, mac_addr: MACAddress, device_name: str, *args, **kwargs):
        self._transform(MAC_ADDR=mac_addr, DEVICE_NAME=device_name, *args, **kwargs)


class ADD_GROUP(BaseCommand):
    """
    Add a group with specified parameters.

    Kwargs:
        - MAC_ADDR (MACAddress, required)
        - BANDWIDTH_MAX_DOWN (int, optional): Maximum Downstream bandwidth
        - BANDWIDTH_MAX_UP (int, optional): Maximum Upstream bandwidth
        - CLASS_NAME (char[64], optional): Class for Class-Based Queuing
        - DHCP_SUBNET (char[10], optional): DHCP subnet
        - QOS_POLICY (str, optional): QoS Policy
        - SMTP_REDIRECT (bool, optional): SMTP Redirection. Default: True
        - USER_DEF1 (char[128], optional): User definable string. Default: empty
        - USER_DEF2 (char[128], optional): User definable string. Default: empty
        - DEVICE_NAME (char[96]): Device name
        - IP6_ADDR (optional): IPv6 address
        - IP_ADDR (optional): IP address
        - PROXY_ARP (optional): Enable/Disable Proxied ARP
        - VLAN (0 ≤ VLAN ≤ 4095, optional): 802.1Q VLAN port
    """

    _type, _spec, *_ = spec.GROUP_ADD

    def __init__(self, mac_addr: MACAddress, *args, **kwargs):
        self._transform(MAC_ADDR=mac_addr, *args, **kwargs)


class ADD_ACCESS_CODE(BaseCommand):
    """
    Add an access code with specified parameters.

    Kwargs:
        - MAC_ADDR (MACAddress, required)
        - BANDWIDTH_MAX_DOWN (int, optional): Maximum Downstream bandwidth
        - BANDWIDTH_MAX_UP (int, optional): Maximum Upstream bandwidth
        - CLASS_NAME (char[64], optional): Class for Class-Based Queuing
        - DHCP_SUBNET (char[10], optional): DHCP subnet
        - QOS_POLICY (str, optional): QoS Policy
        - SMTP_REDIRECT (bool, optional): SMTP Redirection. Default: True
        - USER_DEF1 (char[128], optional): User definable string. Default: empty
        - USER_DEF2 (char[128], optional): User definable string. Default: empty
        - DEVICE_NAME (char[96]): Device name
        - IP6_ADDR (optional): IPv6 address
        - IP_ADDR (optional): IP address
        - PROXY_ARP (optional): Enable/Disable Proxied ARP
        - VLAN (0 ≤ VLAN ≤ 4095, optional): 802.1Q VLAN port
    """

    _type, _spec, *_ = spec.ACCESS_CODE_ADD

    def __init__(self, mac_addr: MACAddress, *args, **kwargs):
        self._transform(MAC_ADDR=mac_addr, *args, **kwargs)
