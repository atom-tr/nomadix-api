# -*- coding: UTF-8 -*-
import pytest

from nseapi.types import FixedList, Char, FixedChar, MACAddress


class TestFixedList:
    @pytest.fixture
    def in_list(self):
        return FixedList("TestList", ["unit1", 2, 1.2])

    def test_call_valid(self, in_list):
        assert in_list("UNIT1") == "unit1"
        assert in_list(2) == 2
        assert in_list(1.2) == 1.2

    def test_call_invalid(self, in_list):
        with pytest.raises(ValueError):
            in_list("invalid_unit")

        with pytest.raises(ValueError):
            in_list("invalid_unit")

    def test_str(self, in_list):
        assert str(in_list) == "TestList(unit1, 2, 1.2)"
        assert in_list.__name__ == "TestList"

    def test_list(self, in_list):
        assert list(in_list) == ["unit1", 2, 1.2]


class TestChar:
    def test_char_creation_valid(self):
        char = Char(5)("test")
        assert char == "test"

    def test_char_creation_invalid(self):
        with pytest.raises(ValueError):
            Char(5)("too_long")
        with pytest.raises(TypeError):
            Char(5)(1.2)


class TestFixedChar:
    def test_fixed_char_creation_valid(self):
        fixed_char = FixedChar(5)("valid")
        assert fixed_char == "valid"

    def test_fixed_char_creation_invalid(self):
        with pytest.raises(ValueError):
            FixedChar(6)("short")
        with pytest.raises(TypeError):
            FixedChar(3)(1.2)


class TestMACAddress:
    @pytest.fixture
    def mac(self):
        return MACAddress("00:1A:2B:3C:4D:5E")

    def test_valid_mac_address(self, mac):
        assert mac[0] == "00"
        assert len(mac) == 6
        assert "001A2B3C4D5E" == str(mac)

    def test_compare(self, mac):
        assert mac == MACAddress("00-1A-2B-3C-4D-5E")
        assert mac != "00-1A-2B-3C-4D-5E"

    def test_invalid_mac_address(self):
        with pytest.raises(ValueError):
            MACAddress("invalid_mac")
