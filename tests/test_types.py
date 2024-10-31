# -*- coding: UTF-8 -*-
import pytest
from nseapi.types import MACAddress


def test_type_mac_address():
    # auto remove ":"
    assert str(MACAddress("11:22:33:44:55:66")) == "112233445566"
    # auto uppercase
    assert str(MACAddress("AA:Bc:cc:44:55:66")) == "AABCCC445566"
    # Exceptions
    with pytest.raises(ValueError):
        MACAddress("wrong:format:of:mac:address")
    with pytest.raises(ValueError):
        MACAddress("11:22:33:44:55")  # missing last segment
    with pytest.raises(ValueError):
        MACAddress("11:22:33:44:55:66:77")  # extra segment
    with pytest.raises(ValueError):
        MACAddress("11:22:33:44:ZZ:66")  # invalid character
