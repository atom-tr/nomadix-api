from nseapi.types import Char, FixedChar, MACAddress

LOGIN = 'RADIUS_LOGIN' , {
    'elements': {
        'SUB_USER_NAME': {
            'type': Char(96), 
            'required': True,
            'help_text': 'Subscriber\'s username'
        },
        'SUB_PASSWORD': {
            'type': Char(128), 
            'required': True,
            'help_text': 'Subscriber\'s password'
        },
        'SUB_MAC_ADDR': {
            'type': MACAddress, 
            'required': True,
            'help_text': 'Subscriber\'s MAC address'
        },
        'PORTAL_SUB_ID': {
            'type': Char(37), 
            'required': False,
            'help_text': 'Unique identifier that the Portal Page web server can send to the NSE which will be sent back with status response'
        },
    }
}

LOGOUT = 'RADIUS_LOGOUT', {
    'elements': {
        'SUB_USER_NAME': {
            'type': Char(96), 
            'required': False,
            'help_text': 'Subscriber\'s username (optional if MAC address is present)'
        },
        'SUB_MAC_ADDR': {
            'type': MACAddress, 
            'required': False,
            'help_text': 'Subscriber\'s MAC address (optional if username is present)'
        },
    }
}