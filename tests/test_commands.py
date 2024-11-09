# -*- coding: UTF-8 -*-
import pytest

from nseapi.types import Command, BaseCommand, FixedChar
from nseapi.commands import CACHE_UPDATE


class TestCommand:
    @pytest.fixture
    def spec(self):
        return {
            "attributes": {
                "ATTR1": {"required": True, "type": str},
                "ATTR2": {"value": "100"},
            },
            "elements": {
                "ELEM1": {"required": True, "type": FixedChar(13), "help_text": "str"},
                "ELEM2": {
                    "required": False,
                    "type": str,
                    "attributes": {
                        "UNIT": {"required": False, "type": str},
                    },
                },
            },
        }

    @pytest.fixture
    def command(self, spec):
        return Command(
            "TestType",
            spec,
            "value1",
            elem1="element_value",
            elem2={"VALUE": "e2", "UNIT": 1},
        )

    def test_command_to_xml(self, command):
        xml_output = command.to_xml()
        assert "COMMAND" in xml_output

    def test_command_validation(self, command):
        command.validate()  # Should not raise an error

    def test_base_command_help(self, command):
        help_text = command.help()
        assert "Help on class TestType" in help_text

    def test_command_invalid_input(self, spec):
        with pytest.raises(TypeError):
            Command("TestType", spec, attr1=1.1, elem1="e").validate()

    # def test_command_missing_required_attribute(self, spec):
    #     with pytest.raises(ValueError, match="ELEM1 is a required element"):
    #         Command("TestType", spec, attr1="value1").to_xml()

    #     with pytest.raises(ValueError):
    #         Command("TestType", spec).validate()


class TestBaseCommand:

    def test_base_command_help(self):
        help_text = CACHE_UPDATE.help()
        assert "Help on class CACHE_UPDATE" in help_text

    def test_base_command_xml(self):
        xml_data = CACHE_UPDATE(
            "00:1A:2B:3C:4D:5E"  # pragma: allowlist secret
        ).to_xml()
        assert 'COMMAND="CACHE_UPDATE" MAC_ADDR="001A2B' in xml_data

    def test_base_command_invalid(self):
        with pytest.raises(ValueError):
            BaseCommand("value1", ELEM1={"VALUE": "element_value"})
