import ipaddress
from nseapi.types import Char, FixedList, MACAddress
from nseapi.commands.options import _bandwidth, _expiry_time, _subscriber

_ADD = {
    "BANDWIDTH_MAX_DOWN": {
        "type": int,
        "required": False,
        "help_text": "Maximum Downstream bandwidth",
    },
    "BANDWIDTH_MAX_UP": {
        "type": int,
        "required": False,
        "help_text": "Maximum Upstream bandwidth",
    },
    "CLASS_NAME": {
        "type": Char(64),
        "required": False,
        "help_text": (
            "Indicates the class that traffic to/from "
            "this user should be assigned to for Class-Based Queuing purposes"
        ),
    },
    "DHCP_SUBNET": {
        "type": Char(10),
        "required": False,
        "help_text": "Subnet based on configured DHCP subnets in the NSE",
    },
    "QOS_POLICY": {
        "type": str,
        "required": False,
        "help_text": (
            "Select and add the QoS Policy that is configured on the NSE "
            "to the profile for the user"
        ),
    },
    "SMTP_REDIRECT": {
        "type": bool,
        "required": False,
        "help_text": "SMTP Redirection Default: TRUE",
    },
    "USER_DEF1": {
        "type": Char(128),
        "required": False,
        "help_text": ("User definable string. Default: empty"),
    },
    "USER_DEF2": {
        "type": Char(128),
        "required": False,
        "help_text": ("User definable string. Default: empty"),
    },
}

SUBSCRIBER_ADD = "SUBSCRIBER_ADD", {
    "attributes": {
        "MAC_ADDR": {"required": False, **_subscriber},
    },
    "elements": {
        **_ADD,
        "BANDWIDTH_DOWN": {
            "type": int,
            "required": False,
            "help_text": (
                "Downstream Bandwidth. "
                "Legacy element that is obsolete because of Bandwidth_Max_Down"
            ),
        },
        "BANDWIDTH_UP": {
            "type": int,
            "required": False,
            "help_text": (
                "Upstream Bandwidth. "
                "Legacy element that is obsolete because of Bandwidth_Max_Up"
            ),
        },
        "CONFIRMATION": {
            "type": Char(10),
            "required": False,
            "help_text": "Confirmation number/ID",
        },
        "COUNTDOWN": {
            "type": FixedList("Countdown", ("0", "1")),
            "required": False,
            "help_text": (
                "0 off, 1 enabled. If not present, defaults to off. "
                "Note: If a billing plan is specified and it is an X-over-Y billing plan, "
                "then the countdown element, if present, is irrelevant and is ignored"
            ),
        },
        "EXPIRY_TIME": {"required": False, **_expiry_time},
        "IP_TYPE": {
            "type": FixedList("IPType", ("PRIVATE", "PUBLIC")),
            "required": False,
            "help_text": "IP type. Either 'PRIVATE' or 'PUBLIC'",
        },
        "PAYMENT": {
            "type": int,
            "required": False,
            "help_text": "Amount charged for access",
        },
        "PAYMENT_METHOD": {
            "type": FixedList(
                "PaymentMethod", ("RADIUS", "PMS", "CREDIT_CARD", "ROOM_OPEN")
            ),
            "required": False,
            "help_text": "Payment method (optional but recommended). ",
        },
        "PLAN": {
            "type": int,
            "required": False,
            "help_text": (
                "Billing plan number. "
                "Relates to the X over Y plan number in Billing Plans setup. "
                "If used for X over Y, USER_NAME and PASSWORD are required"
            ),
        },
        "ROOM_NUMBER": {"type": Char(8), "required": False, "help_text": "Room number"},
        "USER_NAME": {
            "type": Char(96),
            "required": False,
            "help_text": "Subscriber's username",
        },
        "PASSWORD": {
            "type": Char(128),
            "required": False,
            "attributes": {
                "ENCRYPT": {"type": bool, "required": False},
            },
            "help_text": "Subscriber's password. ENCRYPT attribute: Either TRUE or FALSE",
        },
    },
}

DEVICE_ADD = "DEVICE_ADD", {
    "attributes": {
        "MAC_ADDR": {
            "type": MACAddress,
            "required": True,
            "help_text": "Device's MAC address",
        },
    },
    "elements": {
        **_ADD,
        "DEVICE_NAME": {
            "type": Char(96),
            "required": False,
            "help_text": (
                "A short name for the device to assist administrator "
                "or operator recognition of it."
            ),
        },
        "IP6_ADDR": {
            "type": ipaddress.IPv6Address,
            "required": False,
            "help_text": (
                "The IPv6 address associated with the device, if any. "
                "The address must be on the proper IPv6 subnet for the interface "
                "to which the device is (to be) attached in order for the device to be accessible."
            ),
        },
        "IP_ADDR": {
            "type": ipaddress.IPv4Address,
            "required": False,
            "help_text": "The IP address associated with the device, if any.",
        },
        "PROXY_ARP": {
            "type": bool,
            "required": False,
            "help_text": (
                "Enable (TRUE) or disable (FALSE) Proxied ARP for this device."
            ),
        },
        "VLAN": {
            "type": int,
            "required": False,
            "help_text": (
                "802.1Q VLAN port that device is attached to (0 ≤ VLAN ≤ 4095). "
                "If omitted or zero, the device will be granted access no matter "
                "where it has attached; but if a non-zero VLAN is specified, "
                "the device will only be granted access when attached to that VLAN."
            ),
        },
    },
}

GROUP_ADD = "GROUP_ADD", {
    "elements": {
        **_ADD,
        "DHCP_TYPE": {
            "type": FixedList("DHCPType", ("PRIVATE", "PUBLIC")),
            "required": False,
            "help_text": "DHCP type",
        },
        "EXPIRY_TIME": {"required": True, **_expiry_time},
        "GROUP_NAME": {
            "type": Char(96),
            "required": False,
            "help_text": (
                "A short name for the group to assist administrator "
                "or operator recognition of it."
            ),
        },
        "GROUP_USERS_MAX": {
            "type": int,
            "required": False,
            "help_text": ("Maximum number of users in the group. Default: no limit"),
        },
        "PAYMENT": {
            "type": int,
            "required": False,
            "help_text": ("Amount charged for access. Default: no limit"),
        },
        "USER_NAME": {
            "type": Char(96),
            "required": True,
            "help_text": "Group's username.",
        },
        "PASSWORD": {
            "type": Char(128),
            "required": True,
            "attributes": {
                "ENCRYPT": {"type": bool, "required": False},
            },
            "help_text": ("Group's password. ENCRYPT attribute: Either TRUE or FALSE"),
        },
        "VALID_UNTIL": {
            "type": str,
            "required": False,
            "help_text": (
                "The date/time at which this group will cease to exist. "
                "If non-empty, must be expressed in a valid ISO 8601 format. "
                "Absence of this element or an empty string means "
                "the group will have permanent (until administratively deleted) existence. "
                "A date/time that does not lie in the future "
                "(with respect to the NSE's current time) will be rejected as an error. "
                "The granularity of this parameter is in minutes, "
                "so if the ISO 8601 string includes seconds they will be ignored "
                "(i.e., treated as if submitted as 00)."
            ),
        },
    }
}

ACCESS_CODE_ADD = "ACCESS_CODE_ADD", {
    "elements": {
        **_ADD,
        "USER_NAME": {
            "type": Char(96),
            "required": True,
            "help_text": "Access Code's username.",
        },
        "EXPIRY_TIME": {"required": True, **_expiry_time},
        "DHCP_TYPE": {
            "type": FixedList("DHCPType", ("PRIVATE", "PUBLIC")),
            "required": False,
            "help_text": "DHCP type",
        },
        "GROUP_USERS_MAX": {
            "type": int,
            "required": False,
            "help_text": (
                "This will set the maximum number of concurrent users "
                "that can utilize this account. "
                "Must be greater than 0."
            ),
        },
        "VALID_UNTIL": {
            "type": str,
            "required": True,
            "help_text": (
                "The date/time at which this group will cease to exist. "
                "If non-empty, must be expressed in a valid ISO 8601 format. "
                "Absence of this element or an empty string means the group will have permanent (until administratively deleted) existence. "
                "A date/time that does not lie in the future (with respect to the NSE's current time) will be rejected as an error. "
                "The granularity of this parameter is in minutes, so if the ISO 8601 string includes seconds they will be ignored (i.e., treated as if submitted as 00)."
            ),
        },
    }
}

SET_BANDWIDTH_UP = "SET_BANDWIDTH_UP", {
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_UP": {"required": True, **_bandwidth}},
}

SET_BANDWIDTH_DOWN = "SET_BANDWIDTH_DOWN", {
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_DOWN": {"required": True, **_bandwidth}},
}

SET_BANDWIDTH_MAX_DOWN = "SET_BANDWIDTH_MAX_DOWN", {
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_MAX_DOWN": {"required": True, **_bandwidth}},
}

SET_BANDWIDTH_MAX_UP = "SET_BANDWIDTH_MAX_UP", {
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_MAX_UP": {"required": True, **_bandwidth}},
}

USER_PAYMENT = ...

USER_DELETE = "USER_DELETE", {
    "elements": {
        "USER": {
            "type": str,
            "required": True,
            "attributes": {
                "ID_TYPE": {
                    "type": FixedList("IP_TYPE", ["MAC_ADDR", "USER_NAME"]),
                    "required": True,
                }
            },
            "help_text": (
                "ID_TYPE attribute: MAC_ADDR or USER_NAME "
                "MAC_ADDR: Subscriber's MAC address (char[12]) "
                "| USER_NAME: Subscriber's username (char [96)"
            ),
        }
    }
}

DEVICE_DELETE = "DEVICE_DELETE", {
    "attributes": {
        "MAC_ADDR": {
            "type": MACAddress,
            "required": True,
            "help_text": "MAC address of the device",
        }
    }
}

USER_QUERY = "USER_QUERY", {
    "elements": {
        "USER": {
            "type": str,
            "required": True,
            "attributes": {
                "ID_TYPE": {
                    "type": FixedList("IP_TYPE", ["MAC_ADDR", "USER_NAME"]),
                    "required": True,
                }
            },
            "help_text": (
                "ID_TYPE attribute: MAC_ADDR or USER_NAME "
                "MAC_ADDR: Subscriber's MAC address (char[12]) "
                "| USER_NAME: Subscriber's username (char [96)"
            ),
        }
    }
}

SUBSCRIBER_QUERY_CURRENT = "SUBSCRIBER_QUERY_CURRENT", {
    "elements": {"MAC_ADDR": {"required": True, **_subscriber}}
}


SUBSCRIBER_QUERY_AUTH = "SUBSCRIBER_QUERY_AUTH", {
    "elements": {
        "MAC_ADDR": {"required": False, **_subscriber},
        "USER_NAME": {
            "type": Char(96),
            "required": False,
            "help_text": "Subscriber's name",
        },
    }
}

USER_AUTHORIZE = "USER_AUTHORIZE", {
    "attributes": {"MAC_ADDR": {"required": True, **_subscriber}}
}

USER_PURCHASE = ...
