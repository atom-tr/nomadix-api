from nseapi.types import FixedList, MACAddress

_bandwidth = {
    "type": int,
    "help_text": "Number measured in Kbps (i.e. for 128,000 bits per second, enter 128)",
}

_subscriber = {
    "type": MACAddress,
    "help_text": "Subscriber's MAC address",
}

_time_unit = {
    "type": FixedList("TimeUnit", ("DAYS", "HOURS", "MINUTES", "SECONDS")),
    "required": False,
}

_expiry_time = {
    "type": int,
    "attributes": {"UNITS": _time_unit},
    "help_text": (
        "Expiry time. UNITS attribute: Either SECONDS, MINUTES, HOURS or DAYS"
    ),
}
