# -*- coding: UTF-8 -*-
import re
from collections.abc import Sequence
from typing import TypeVar

import xmltodict

from nseapi.utils import generate_docstring


class FixedList:
    def __init__(self, name: str, units: list):
        self.name = name
        self.units = units if isinstance(units, list) else [units]

    def _str_list(self):
        return ", ".join(str(unit) for unit in self.units)

    def __call__(self, value):
        for unit in self.units:
            if isinstance(unit, (str, int)) and isinstance(value, (str, int)):
                if re.match(re.escape(str(unit)), str(value), re.IGNORECASE):
                    return unit
            elif unit == value:
                return unit
        raise ValueError(f"Value must be one of {self._str_list()}")

    def __str__(self):
        return f"{self.name}({self._str_list()})"

    @property
    def __name__(self):
        return self.name

    def __iter__(self):
        return iter(self.units)


T = TypeVar("T", bound=str)


class Char:
    def __new__(cls, max_length: int):
        class VarChar(str):
            def __new__(cls, value: str) -> "VarChar":
                if not isinstance(value, str):
                    raise TypeError(
                        f"Value must be a string, not {type(value).__name__}"
                    )
                if len(value) > max_length:
                    raise ValueError(
                        f"String length must be at most {max_length} characters"
                    )
                return str.__new__(cls, value)

        VarChar.__name__ = f"Char({max_length})"
        return VarChar


class FixedChar:
    def __new__(cls, size: int):
        class FixedChar(str):
            def __new__(cls, value: str) -> "FixedChar":
                if not isinstance(value, str):
                    raise TypeError(
                        f"Value must be a string, not {type(value).__name__}"
                    )
                if len(value) != size:
                    raise ValueError(f"String length must be exactly {size} characters")
                return str.__new__(cls, value)

        FixedChar.__name__ = f"FixedChar({size})"
        return FixedChar


class MACAddress(Sequence):
    _regex = re.compile(r"^([0-9A-Fa-f]{2}([-:]?)){5}([0-9A-Fa-f]{2})$")

    def __init__(self, addr: str):
        if not self._is_valid(addr):
            raise ValueError("Not a valid MAC address")

        # Normalize the address by removing separators and converting to uppercase
        self._addr = addr.upper().replace(":", "").replace("-", "")

        # Store the address as a list of 2-character segments for immutability
        self._segments = [self._addr[i : i + 2] for i in range(0, 12, 2)]

    def _is_valid(self, addr: str) -> bool:
        return bool(self._regex.match(addr))

    def __getitem__(self, index):
        return self._segments[index]

    def __len__(self):
        return len(self._segments)

    def __str__(self):
        return self.formatted("")

    def __repr__(self):  # pragma: no cover
        return f"MACAddress({self.formatted('')})"

    def __eq__(self, other):
        if not isinstance(other, MACAddress):
            return NotImplemented
        return self._addr == other._addr

    def formatted(self, separator=":"):
        # Join the segments with the specified separator
        return separator.join(self._segments)


class Command:

    _input_data = {}

    def __init__(self, _type, _spec, *args, **kwargs):
        self._type = _type
        self._spec = _spec
        self._transform(*args, **kwargs)

    def __str__(self) -> str:  # pragma: no cover
        return self.to_xml()

    def _transform(self, *args, **kwargs):
        """Transform input to dictionary based on command spec"""
        # cleanup kwargs
        cleaned_kwargs = {
            k.upper(): (
                v
                if not isinstance(v, dict)
                else {sk.upper(): sv for sk, sv in v.items()}
            )
            for k, v in kwargs.items()
        }
        # mapping args to kwargs
        if args:
            attribute_keys = list(self._spec.get("attributes", {}).keys())
            element_keys = list(self._spec.get("elements", {}).keys())
            _keys = (
                _
                for _ in attribute_keys + element_keys
                if _ not in cleaned_kwargs.keys()
            )
            self._input_data.update(zip(_keys, args))

        self._input_data.update(cleaned_kwargs)

    def validate(self):
        for key, spec in self._spec.get("attributes", {}).items():
            if "value" in spec:
                continue
            if spec["required"] and key not in self._input_data:
                raise ValueError(f"Attribute {key} is required for {self._type}")
            if key in self._input_data:
                self._validate_value(key, spec)

        for key, spec in self._spec.get("elements", {}).items():
            if spec["required"] and key not in self._input_data:
                raise ValueError(f"Element {key} is required for {self._type}")
            if key in self._input_data:
                self._validate_value(key, spec, is_element=True)

    def _validate_value(self, key, spec, is_element=False):
        value = self._input_data[key]
        try:
            if is_element and isinstance(value, dict):
                element_value = value.get("VALUE", "")
                value["VALUE"] = spec.get("type", str)(element_value)
                if "attributes" in spec:
                    for attr_key, attr_spec in spec["attributes"].items():
                        if attr_key in value:
                            value[attr_key] = attr_spec.get("type", str)(
                                value[attr_key]
                            )
            else:
                self._input_data[key] = spec.get("type", str)(value)
        except (TypeError, ValueError) as e:
            raise TypeError(f"{key}: {str(e)}")

    def to_xml(self):
        self.validate()
        usg_dict = {"@COMMAND": self._type}
        for key, spec in self._spec.get("attributes", {}).items():
            if key in self._input_data:
                usg_dict[f"@{key}"] = str(self._input_data[key])
            elif "value" in spec:
                usg_dict[f"@{key}"] = str(spec["value"])

        for key in self._spec.get("elements", {}):
            if key in self._input_data:
                element_value = self._input_data[key]
                if isinstance(element_value, dict):
                    element_dict = {"#text": str(element_value.pop("VALUE", ""))}
                    for attr_key, attr_value in element_value.items():
                        element_dict[f"@{attr_key}"] = str(attr_value)
                    usg_dict[key] = element_dict
                else:
                    usg_dict[key] = str(element_value)
        return xmltodict.unparse({"USG": usg_dict}, pretty=True)

    def help(self):
        """Generate help text for the command."""
        return f"Help on class {self._type}:\n" + generate_docstring(self._spec)


class BaseCommand(Command):

    def __init__(self, *args, **kwargs):
        if hasattr(self, "_type") and hasattr(self, "_spec"):
            self._transform(*args, **kwargs)  # pragma: no cover
        else:
            raise ValueError("Both _type and _spec must be defined.")

    @classmethod
    def help(cls):
        """Generate help text for the command."""
        return f"Help on class {cls._type}:\n" + generate_docstring(cls._spec)
