from nseapi.types import CharArray, FixedCharArray

LOGIN = {
    'attributes': {
        'COMMAND': 'RADIUS_LOGIN'
    },
    'elements': {
        'SUB_USER_NAME': {
            'type': CharArray(96), 
            'required': True,
            'help_text': 'Subscriber\'s username (char [96], required)'
        },
        'SUB_PASSWORD': {
            'type': CharArray(128), 
            'required': True,
            'help_text': 'Subscriber\'s password (char [128], required)'
        },
        'SUB_MAC_ADDR': {
            'type': FixedCharArray(12), 
            'required': True,
            'help_text': 'Subscriber\'s MAC address (char [12], required)'
        },
        'PORTAL_SUB_ID': {
            'type': CharArray(37), 
            'required': False,
            'help_text': 'Unique identifier that the Portal Page web server can send to the NSE which will be sent back with status response (char [37], optional)'
        },
    }
}

LOGOUT = {
    'attributes': {
        'COMMAND': 'RADIUS_LOGOUT'
    },
    'elements': {
        'SUB_USER_NAME': {
            'type': CharArray(96), 
            'required': False,
            'help_text': 'Subscriber\'s username (char [96], optional if MAC address is present)'
        },
        'SUB_MAC_ADDR': {
            'type': FixedCharArray(12), 
            'required': False,
            'help_text': 'Subscriber\'s MAC address (char [12], optional if username is present)'
        },
    }
}