from nseapi.types import CharArray, FixedCharArray


LOGIN = {
    'COMMAND': 'RADIUS_LOGIN',
    'required': (
        ('SUB_USER_NAME', CharArray(96)),
        ('SUB_PASSWORD', CharArray(128)),
        ('SUB_MAC_ADDR', FixedCharArray(12)),
    ),
    'optional': (
        ('PORTAL_SUB_ID', CharArray(37)),
    ),
}
"""
COMMAND attribute: ‘RADIUS_LOGIN’ 
SUB_USER_NAME: Subscriber’s username (char [96]) 
SUB_PASSWORD: Subscriber’s password (char [128]) 
SUB_MAC_ADDR: Subscriber’s MAC address (char [12]) 
PORTAL_SUB_ID (optional): Unique identifier that the Portal Page web server can send to the 
NSE which will be sent back with status response (char [36])
"""


LOGOUT = {
    'COMMAND': 'LOGOUT',
    'required': (),
    'optional': (
        ('SUB_USER_NAME', CharArray(96)),
        ('SUB_MAC_ADDR', FixedCharArray(12)),
    ),
}
"""
COMMAND attribute: ‘LOGOUT’ 
SUB_MAC_ADDR: Subscriber’s MAC address (char [12], optional if username is present) 
SUB_USER_NAME: Subscriber’s username (char [96], optional if MAC address is present) 
"""