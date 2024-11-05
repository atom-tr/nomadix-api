from nseapi.types import Char, FixedList, MACAddress
from nseapi.commands.options import _expiry_time

USER_PAYMENT = "USER_PAYMENT", {
    "attributes": {"PAYMENT_METHOD": {"value": "PMS"}},
    "elements": {
        "USER_NAME": {
            "type": Char(96),
            "required": True,
            "help_text": (
                "Subscriber's username. For 2-way PMS, "
                "the subscriber's MAC address is optional but recommended."
            ),
        },
        "REAL_NAME": {
            "type": Char(96),
            "required": False,
            "help_text": (
                "Subscriber's real name as listed in PMS (char [1]). "
                "Required for 2-way PMS"
            ),
        },
        "PASSWORD": {
            "type": Char(128),
            "required": True,
            "attributes": {
                "ENCRYPT": {"type": bool, "required": False},
            },
            "help_text": "Password. ENCRYPT attribute: Either TRUE or FALSE",
        },
        "EXPIRY_TIME": {"required": False, **_expiry_time},
        "ROOM_NUMBER": {
            "type": Char(8),
            "required": True,
            "help_text": "Room number of access. For 2-way PMS, use the PMS database room number.",
        },
        "PAYMENT": {
            "type": float,
            "required": False,
            "help_text": "Amount charged for access",
        },
        "MAC_ADDR": {
            "type": MACAddress,
            "required": True,
            "help_text": "MAC address of user for post-paid PMS and 2-way PMS (char [3]).",
        },
        "REG_NUMBER": {
            "type": Char(24),
            "required": True,
            "help_text": "Reservation number of hotel guest for Micros Fidelio FIAS compliant Query and Post interface.",
        },
        "BANDWIDTH_MAX_UP": {
            "type": int,
            "required": False,
            "help_text": "This will set the Maximum Upstream bandwidth for the user without having to send any other Bandwidth XML Command.",
        },
        "BANDWIDTH_MAX_DOWN": {
            "type": int,
            "required": False,
            "help_text": "This will set the Maximum Downstream bandwidth for the user without having to send any other Bandwidth XML Command.",
        },
        "COUNTDOWN": {
            "type": bool,
            "required": False,
            "help_text": "This will set the user so that their allotted time will not start counting down, and the charge will not post, until they log in (note: only supported for 1-way PMS systems).",
        },
        "BILLING_PLAN": {
            "type": int,
            "required": False,
            "help_text": "This will allow selection of a specified billing plan for either an X over Y Setting or a WFB selection for the user.",
        },
        "CC_SUFFIX": {
            "type": str,
            "required": False,
            "help_text": "Last 4 Digits of the Credit Card for Marriott WFB PMS Verification.",
        },
        "CC_EXPIRATION": {
            "type": str,
            "required": False,
            "help_text": "Expiration Date on the Credit Card for Marriott WFB PMS Verification. Format = MMYY.",
        },
        "WFB_BUNDLED": {
            "type": int,
            "required": False,
            "help_text": (
                "WFB Bundle Bill. 0 = Charge 1 = Bundle. "
                "WFB_OPTION: Either A, B, C or D"
            ),
            "attributes": {
                "WFB_OPTION": {
                    "type": FixedList("WFB", ("A", "B", "C", "D")),
                    "required": False,
                }
            },
        },
        "TRANS_ID": {
            "type": int,
            "required": False,
            "help_text": "(32 bit unsigned Integer) Used to match commands with USER_STATUS messages. Information entered here will be mirrored on the USER_STATUS messages.",
        },
        "REVENUE_CENTER": {
            "type": str,
            "required": False,
            "help_text": "3 Digits to specify the Revenue Center for MICROS PMS, or 2 Digits to specify Revenue Code for Marriott WFB and Marriott FOSSE.",
        },
        "CLASS_NAME": {
            "type": Char(64),
            "required": False,
            "help_text": "Class name (char [5]) indicates the class that traffic to/from this subscriber should be assigned to for Class-Based Queuing purposes.",
        },
    },
}

USER_PURCHASE = "USER_PURCHASE", {
    "attributes": {
        "ROOM_NUMBER": {
            "type": Char(8),
            "required": True,
            "help_text": "Room number (Port-Location 'Location' number), (char [2])",
        },
    },
    "elements": {
        "ITEM_CODE": {
            "type": str,
            "required": True,
            "help_text": "Code of the item being purchased",
        },
        "ITEM_DESCRIPTION": {
            "type": str,
            "required": True,
            "help_text": "Description of the item",
        },
        "ITEM_AMOUNT": {
            "type": float,
            "required": True,
            "help_text": "Item amount",
        },
        "ITEM_TAX": {
            "type": float,
            "required": True,
            "help_text": "Item tax",
        },
        "ITEM_TOTAL": {
            "type": float,
            "required": True,
            "help_text": "Item total",
        },
        "REAL_NAME": {
            "type": str,
            "required": True,
            "help_text": "Name in the PMS DATABASE Only needed for 2-way PMS",
        },
        "MAC_ADDRESS": {
            "type": MACAddress,
            "required": False,
            "help_text": "MAC Address of the Subscriber Only needed for Post Paid PMS",
        },
        "REG_NUMBER": {
            "type": str,
            "required": True,
            "help_text": "Registration number required for 2-way FIAS PMS",
        },
        "CC_SUFFIX": {
            "type": str,
            "required": False,
            "help_text": "Last 4 Digits of the Credit Card for Marriott WFB PMS Verification.",
        },
        "CC_EXPIRATION": {
            "type": str,
            "required": False,
            "help_text": "Expiration Date on the Credit Card for Marriott WFB PMS Verification. Format = MMYY.",
        },
        "WFB_BUNDLED": {
            "type": int,
            "required": False,
            "help_text": (
                "WFB Bundle Bill. 0 = Charge 1 = Bundle. "
                "WFB_OPTION: Either A, B, C or D"
            ),
            "attributes": {
                "WFB_OPTION": {
                    "type": FixedList("WFB", ("A", "B", "C", "D")),
                    "required": False,
                }
            },
        },
        "TRANS_ID": {
            "type": int,
            "required": False,
            "help_text": "unsigned Integer) Used to match commands with USER_STATUS messages. Information entered here will be mirrored on the USER_STATUS messages. ",
        },
        "REVENUE_CENTER": {
            "type": str,
            "required": False,
            "help_text": "3 Digits to specify the Revenue Center for MICROS PMS, or 2 Digits to specify Revenue Code for Marriott WFB and Marriott FOSSE.",
        },
    },
}

PMS_PENDING_TRANSACTION = "PMS_PENDING_TRANSACTION", {
    "elements": {
        "TRANSACTION_ID": {
            "type": int,
            "required": False,
            "help_text": "(32 bit unsigned Integer) Used to match commands with PMS_TRANSACTION_RESPONSE messages. Information entered here will be mirrored on the PMS_TRANSACTION_RESPONSE messages.",
        },
        "DATA": {
            "type": str,
            "required": True,
            "help_text": "The data that will be sent to the attached PMS system.  Before sending, the data is framed with an ETX (hex 02) and an STX (hex 03) and appended with a checksum.",
        },
    },
}

ROOM_SET_ACCESS = "ROOM_SET_ACCESS", {
    "attributes": {
        "ROOM_NUMBER": {
            "type": Char(8),
            "required": True,
            "help_text": "Room number (Port-Location 'Location' number)",
        },
    },
    "elements": {
        "ACCESS_MODE": {
            "type": FixedList(
                "ACCESS_MODE", ("ROOM_OPEN", "ROOM_CHARGE", "ROOM_BLOCK")
            ),
            "required": True,
            "help_text": "Either ROOM_OPEN, ROOM_CHARGE, or ROOM_BLOCK",
        },
    },
}

ROOM_QUERY_ACCESS = "ROOM_QUERY_ACCESS", {
    "elements": {
        "ROOM_NUMBER": {
            "type": Char(8),
            "required": True,
            "help_text": "Room number (Port-Location 'Location' number)",
        },
    },
}
