from nseapi.types import MACAddress, BaseCommand
from nseapi.commands.options import radius as spec

__all__ = ("LOGIN", "LOGOUT")


class LOGIN(BaseCommand):
    """
    Initiates RADIUS authentication via Portal Page web server.

    Kwargs:
        - SUB_USER_NAME: Subscriber's username (char [96])
        - SUB_PASSWORD: Subscriber's password (char [128])
        - SUB_MAC_ADDR: Subscriber's MAC address (char [12])
        - PORTAL_SUB_ID (optional): Unique identifier for status response (char [36])
    """

    _type, _spec, *_ = spec.LOGIN

    def __init__(
        self,
        sub_user_name: str,
        sub_password: str,
        sub_mac_addr: MACAddress,
        *args,
        **kwargs
    ):
        self._transform(
            sub_user_name=sub_user_name,
            sub_password=sub_password,
            sub_mac_addr=sub_mac_addr,
            *args,
            **kwargs
        )


class LOGOUT(BaseCommand):
    """
    Command to logout a subscriber.

    Kwargs:
        - SUB_USER_NAME: Subscriber's username (char [96])
        - SUB_MAC_ADDR: Subscriber's MAC address (char [12])
    """

    _type, _spec, *_ = spec.LOGOUT

    def __init__(self, sub_user_name: str, sub_mac_addr: MACAddress):
        self._transform(sub_user_name=sub_user_name, sub_mac_addr=sub_mac_addr)
