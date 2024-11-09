from nseapi.types import MACAddress, BaseCommand
from nseapi.commands.options import network as spec


class SET_BANDWIDTH_UP(BaseCommand):
    """
    Set the Bandwidth Up for an authorized subscriber.

    Kwargs:
        - subscriber: Subscriber's MAC address
        - bandwidth_up: Number measured in Kbps
            (i.e. for 128,000 bits per second, enter 128)
    """

    _type, _spec, *_ = spec.SET_BANDWIDTH_UP

    def __init__(self, subscriber: MACAddress, bandwidth_up: int):
        self._transform(SUBSCRIBER=subscriber, BANDWIDTH_UP=bandwidth_up)


class SET_BANDWIDTH_DOWN(BaseCommand):
    """
    Sets the downstream bandwidth for an authorized subscriber.
    """

    _type, _spec, *_ = spec.SET_BANDWIDTH_DOWN


class SET_BANDWIDTH_MAX_UP(BaseCommand):
    """
    Sets the guaranteed maximum downstream bandwidth for an authorized subscriber
    """

    _type, _spec, *_ = spec.SET_BANDWIDTH_MAX_UP


class SET_BANDWIDTH_MAX_DOWN(BaseCommand):
    """
    Sets the guaranteed maximum upstream bandwidth for an authorized subscriber.
    """

    _type, _spec, *_ = spec.SET_BANDWIDTH_MAX_DOWN


# class DAT_TABLE_RSP(BaseCommand):
#     """
#     Provides the Dynamic Address Translation (DAT) table, which shows the network address translation information for active sessions
#     """

#     _type, _spec, *_ = spec.DAT_TABLE_RSP


# class ACTIVE_ROUTES(BaseCommand):
#     """
#     Lists active routes in the routing table
#     """

#     _type, _spec, *_ = spec.ACTIVE_ROUTES


# class PERSISTENT_ROUTES(BaseCommand):
#     """
#     Lists persistent routes that are saved in the device's configuration and are restored after a reboot.
#     """

#     _type, _spec, *_ = spec.PERSISTENT_ROUTES


# class STATIC_ROUTES(BaseCommand):
#     """
#     Lists static routes that are configured manually and are not saved in persistent storage
#     """

#     _type, _spec, *_ = spec.STATIC_ROUTES


# class CBQUEUEING_CLASS(BaseCommand):
#     """
#     Manages Class-Based Queuing (CBQ) classes, which allow for prioritizing and controlling network traffic based on different criteria
#     """

#     _type, _spec, *_ = spec.CBQUEUEING_CLASS


# class WAN_STATUS(BaseCommand):
#     """
#     Reports the status of the primary WAN interface
#     """

#     _type, _spec, *_ = spec.WAN_STATUS
