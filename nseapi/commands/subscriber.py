from nseapi.types import CharArray, FixedCharArray, FixedList

_ADD = {
    'attributes': {
        'MAC_ADDR': {'type': FixedCharArray(12), 'required': False},
    },
    'elements': {
        'BANDWIDTH_MAX_DOWN': {
            'type': int, 
            'required': False,
            'help_text': "Maximum Downstream bandwidth (int, optional)"
        },
        'BANDWIDTH_MAX_UP': {
            'type': int, 
            'required': False,
            'help_text': "Maximum Upstream bandwidth (int, optional)"
        },
        'CLASS_NAME': {
            'type': CharArray(64), 
            'required': False,
            'help_text': "Class name (char [64], optional). Indicates the class that traffic to/from this user should be assigned to for Class-Based Queuing purposes"
        },
        'DHCP_SUBNET': {
            'type': CharArray(10), 
            'required': False,
            'help_text': "DHCP subnet (char [10], optional). Subnet based on configured DHCP subnets in the NSE"
        },
        'QOS_POLICY': {
            'type': str, 
            'required': False,
            'help_text': "QoS Policy (str, optional). Select and add the QoS Policy that is configured on the NSE to the profile for the user"
        },
        'SMTP_REDIRECT': {
            'type': bool, 
            'required': False,
            'help_text': "SMTP Redirection (bool, optional). Either TRUE or FALSE. If not included, the User will have this variable as TRUE for their profile"
        },
        'USER_DEF1': {
            'type': CharArray(128), 
            'required': False,
            'help_text': "User definable string (char [128], optional). If not provided, NSE will empty it"
        },
        'USER_DEF2': {
            'type': CharArray(128), 
            'required': False,
            'help_text': "User definable string (char [128], optional). If not provided, NSE will empty it"
        },
    }
}

SUBSCRIBER_ADD = _ADD
SUBSCRIBER_ADD['attributes']['COMMAND'] = 'SUBSCRIBER_ADD'
SUBSCRIBER_ADD['elements'].update({
    'BANDWIDTH_DOWN': {
        'type': int, 
        'required': False,
        'help_text': "Downstream Bandwidth (int, optional). Legacy element that is obsolete because of Bandwidth_Max_Down"
    },
    'BANDWIDTH_UP': {
        'type': int, 
        'required': False,
        'help_text': "Upstream Bandwidth (int, optional). Legacy element that is obsolete because of Bandwidth_Max_Up"
    },
    'CONFIRMATION': {
        'type': CharArray(10), 
        'required': False,
        'help_text': "Confirmation number/ID (char [10], optional)"
    },
    'COUNTDOWN': {
        'type': FixedList('Countdown', ('0', '1')), 
        'required': False,
        'help_text': "Countdown (int, optional). 0 off, 1 enabled. If not present, defaults to off. Note: If a billing plan is specified and it is an X-over-Y billing plan, then the countdown element, if present, is irrelevant and is ignored"
    },
    'EXPIRY_TIME': {
        'type': int, 
        'required': False,
        'attributes': {
            'UNITS': {
                'type': FixedList('TimeUnit', ('DAYS', 'HOURS', 'MINUTES', 'SECONDS')), 
                'required': False
            },
        },
        'help_text': "Expiry time (optional). UNITS attribute: Either SECONDS, MINUTES, HOURS or DAYS"
    },
    'IP_TYPE': {
        'type': FixedList('IPType', ('PRIVATE', 'PUBLIC')), 
        'required': False,
        'help_text': "IP type (char [10], optional). Either 'PRIVATE' or 'PUBLIC'"
    },
    'PAYMENT': {
        'type': int, 
        'required': False,
        'help_text': "Amount charged for access (int, optional)"
    },
    'PAYMENT_METHOD': {
        'type': FixedList('PaymentMethod', ('RADIUS', 'PMS', 'CREDIT_CARD', 'ROOM_OPEN')), 
        'required': False,
        'help_text': "Payment method (char [10], optional but recommended). Either 'RADIUS', 'PMS', 'CREDIT_CARD', or 'ROOM_OPEN'"
    },
    'PLAN': {
        'type': int, 
        'required': False,
        'help_text': "Billing plan number (int, optional). Relates to the X over Y plan number in Billing Plans setup. If used for X over Y, USER_NAME and PASSWORD are required"
    },
    'ROOM_NUMBER': {
        'type': CharArray(8), 
        'required': False,
        'help_text': "Room number (char [8], optional)"
    },
    'USER_NAME': {
        'type': CharArray(96), 
        'required': False,
        'help_text': "Subscriber's username (char [96], optional)"
    },
    'PASSWORD': {
        'type': CharArray(128), 
        'required': False,
        'attributes': {
            'ENCRYPT': {'type': bool, 'required': False},
        },
        'help_text': "Subscriber's password (char [128], optional). ENCRYPT attribute: Either TRUE or FALSE"
    },
})


DEVICE_ADD = _ADD
DEVICE_ADD['attributes']['COMMAND'] = 'DEVICE_ADD'
DEVICE_ADD['elements'].update({
    'DEVICE_NAME': {
        'type': CharArray(96), 
        'required': False,
        'help_text': "A short name for the device (char[96]) to assist administrator or operator recognition of it."
    },
    'IP6_ADDR': {
        'type': CharArray(45), 
        'required': False,
        'help_text': "The IPv6 address associated with the device, if any. The address must be on the proper IPv6 subnet for the interface to which the device is (to be) attached in order for the device to be accessible."
    },
    'IP_ADDR': {
        'type': CharArray(16), 
        'required': False,
        'help_text': "The IP address associated with the device, if any."
    },
    'PROXY_ARP': {
        'type': bool, 
        'required': False,
        'help_text': "Enable (TRUE) or disable (FALSE) Proxied ARP for this device."
    },
    'VLAN': {
        'type': int, 
        'required': False,
        'help_text': "802.1Q VLAN port that device is attached to (0 ≤ VLAN ≤ 4095). If omitted or zero, the device will be granted access no matter where it has attached; but if a non-zero VLAN is specified, the device will only be granted access when attached to that VLAN."
    },
})

GROUP_ADD = _ADD
GROUP_ADD['attributes'] = {'COMMAND': 'GROUP_ADD'}
GROUP_ADD['elements'].update({
    'DHCP_TYPE': {
        'type': FixedList('DHCPType', ('PRIVATE', 'PUBLIC')), 
        'required': False,
        'help_text': "DHCP type (char[10], optional). Either 'PRIVATE', 'PUBLIC'"
    },
    'EXPIRY_TIME': {
        'type': int, 
        'required': True,
        'attributes': {
            'UNITS': {
                'type': FixedList('TimeUnit', ('DAYS', 'HOURS', 'MINUTES', 'SECONDS')), 
                'required': False
            },
        },
        'help_text': "Expiry time (optional). UNITS attribute: Either SECONDS, MINUTES, HOURS or DAYS"
    },
    'GROUP_NAME': {
        'type': CharArray(96), 
        'required': False,
        'help_text': "A short name for the group (char[96]) to assist administrator or operator recognition of it."
    },
    'GROUP_USERS_MAX': {
        'type': int, 
        'required': False,
        'help_text': "Maximum number of users in the group (int, optional). If not specified, the group will be created with no limit on the number of users."
    },
    'PAYMENT': {
        'type': int, 
        'required': False,
        'help_text': "Amount charged for access (int, optional). If not specified, the group will be created with no limit on the number of users."
    },
    'USER_NAME': {
        'type': CharArray(96), 
        'required': True,
        'help_text': "Group's username (char[96])."
    },
    'PASSWORD': {
        'type': CharArray(128), 
        'required': True,
        'attributes': {
            'ENCRYPT': {'type': bool, 'required': False},
        },
        'help_text': "Group's password (char[128]). ENCRYPT attribute: Either TRUE or FALSE"
    },
    'VALID_UNTIL': {
        'type': str, 
        'required': False,
        'help_text': "The date/time at which this group will cease to exist. If non-empty, must be expressed in a valid ISO 8601 format. Absence of this element or an empty string means the group will have permanent (until administratively deleted) existence. A date/time that does not lie in the future (with respect to the NSE's current time) will be rejected as an error. The granularity of this parameter is in minutes, so if the ISO 8601 string includes seconds they will be ignored (i.e., treated as if submitted as 00)."
    },
})

ACCESS_CODE_ADD = _ADD
ACCESS_CODE_ADD['attributes'] = {'COMMAND': 'ACCESS_CODE_ADD'}
ACCESS_CODE_ADD['elements'].update({
    'USER_NAME': {
        'type': CharArray(96), 
        'required': True,
        'help_text': "Group's username (char[96])."
    },
    'EXPIRY_TIME': {
        'type': int, 
        'required': True,
        'attributes': {
            'UNITS': {
                'type': FixedList('TimeUnit', ('DAYS', 'HOURS', 'MINUTES', 'SECONDS')), 
                'required': False
            },
        },
    },
    'DHCP_TYPE': {
        'type': FixedList('DHCPType', ('PRIVATE', 'PUBLIC')), 
        'required': False,
        'help_text': "DHCP type (char[10], optional). Either 'PRIVATE', 'PUBLIC'"
    },
    'GROUP_USERS_MAX': {
        'type': int, 
        'required': False,
        'help_text': "This will set the maximum number of concurrent users that can utilize this account. Must be greater than 0."
    },
    'VALID_UNTIL': {
        'type': str, 
        'required': True,
        'help_text': "The date/time at which this group will cease to exist. If non-empty, must be expressed in a valid ISO 8601 format. Absence of this element or an empty string means the group will have permanent (until administratively deleted) existence. A date/time that does not lie in the future (with respect to the NSE's current time) will be rejected as an error. The granularity of this parameter is in minutes, so if the ISO 8601 string includes seconds they will be ignored (i.e., treated as if submitted as 00)."
    },
})