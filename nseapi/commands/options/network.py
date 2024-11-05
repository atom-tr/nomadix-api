from nseapi.commands.options import _bandwidth, _subscriber

SET_BANDWIDTH_UP = "SET_BANDWIDTH_UP", {  # Moved from subscriber
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_UP": {"required": True, **_bandwidth}},
}

SET_BANDWIDTH_DOWN = "SET_BANDWIDTH_DOWN", {  # Moved from subscriber
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_DOWN": {"required": True, **_bandwidth}},
}

SET_BANDWIDTH_MAX_DOWN = "SET_BANDWIDTH_MAX_DOWN", {  # Moved from subscriber
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_MAX_DOWN": {"required": True, **_bandwidth}},
}

SET_BANDWIDTH_MAX_UP = "SET_BANDWIDTH_MAX_UP", {  # Moved from subscriber
    "attributes": {"SUBSCRIBER": {"required": True, **_subscriber}},
    "elements": {"BANDWIDTH_MAX_UP": {"required": True, **_bandwidth}},
}

DAT_TABLE_RSP = ...

ACTIVE_ROUTES = ...

PERSISTENT_ROUTES = ...

STATIC_ROUTES = ...

CBQUEUEING_CLASS = ...

WAN_STATUS = ...
