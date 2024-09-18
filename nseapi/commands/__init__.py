from . import radius as _radius
from . import subscriber as _subscriber
from nseapi.types import Command, FixedCharArray

__all__ = ['Radius', 'Subscriber', 'CACHE_UPDATE']

class Radius:
    LOGIN = lambda **kwargs: Command('RADIUS_LOGIN', _radius.LOGIN, **kwargs)
    LOGOUT = lambda **kwargs: Command('RADIUS_LOGOUT', _radius.LOGOUT, **kwargs)

class Subscriber:
    ADD_USER = lambda **kwargs: Command('SUBSCRIBER_ADD', _subscriber.SUBSCRIBER_ADD, **kwargs)
    ADD_DEVICE = lambda **kwargs: Command('DEVICE_ADD', _subscriber.DEVICE_ADD, **kwargs)
    ADD_GROUP = lambda **kwargs: Command('GROUP_ADD', _subscriber.GROUP_ADD, **kwargs)
    ADD_ACCESS_CODE = lambda **kwargs: Command('ACCESS_CODE_ADD', _subscriber.ACCESS_CODE_ADD, **kwargs)

CACHE_UPDATE = lambda **kwargs: Command('CACHE_UPDATE', {
    'attributes': {
        'COMMAND': 'CACHE_UPDATE',
        'MAC_ADDR': {'type': FixedCharArray(12), 'required': True},
    }
}, **kwargs)
