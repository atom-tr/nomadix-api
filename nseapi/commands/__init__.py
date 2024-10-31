from nseapi.types import MACAddress, BaseCommand
from . import radius
from . import subscriber

__all__ = ["radius", "subscriber", "CACHE_UPDATE"]


class CACHE_UPDATE(BaseCommand):
    """
    Updates the memory authorization table entry
    for a subscriber's MAC address from "pending" to "authorized".
    This is crucial for enabling proper access.

    Kwargs:
        - mac_addr: Subscriber's MAC address
    """

    _type = "CACHE_UPDATE"
    _spec = {
        "attributes": {
            "MAC_ADDR": {"type": MACAddress, "required": True},
        }
    }

    def __init__(self, mac_addr: str):
        self._transform(MAC_ADDR=mac_addr)
