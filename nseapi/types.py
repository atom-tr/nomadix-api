# -*- coding: UTF-8 -*-
import re
from collections.abc import Sequence
from typing import Generic, TypeVar, List, Type
from enum import Enum, auto

import xmltodict


class FixedList:
    def __init__(self, name, units):
        self.name = name
        self.units = tuple(u.upper() for u in units)

    def __call__(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Value must be a string, not {type(value).__name__}")
        upper_value = value.upper()
        for unit in self.units:
            if unit.startswith(upper_value):
                return unit
        raise ValueError(f"Value must be one of {', '.join(self.units)}")

    def __str__(self):
        return f"{self.name}({', '.join(self.units)})"

    def list(self):
        return list(self.units)

T = TypeVar('T', bound=str)

class CharArray:
    def __new__(cls, max_length: int):
        class VarChar(str):
            def __new__(cls, value: str) -> 'VarChar':
                if not isinstance(value, str):
                    raise TypeError(f"Value must be a string, not {type(value).__name__}")
                if len(value) > max_length:
                    raise ValueError(f"String length must be at most {max_length} characters")
                return str.__new__(cls, value)
        VarChar.__name__ = f'CharArray({max_length})'
        return VarChar

class FixedCharArray:
    def __new__(cls, size: int):
        class FixedChar(str):
            def __new__(cls, value: str) -> 'FixedChar':
                if not isinstance(value, str):
                    raise TypeError(f"Value must be a string, not {type(value).__name__}")
                if len(value) != size:
                    raise ValueError(f"String length must be exactly {size} characters")
                return str.__new__(cls, value)
        FixedChar.__name__ = f'FixedCharArray({size})'
        return FixedChar
    
class MACAddress(Sequence):
    _regex = re.compile(r'^([0-9A-Fa-f]{2}([-:]?)){5}([0-9A-Fa-f]{2})$')

    def __init__(self, addr: str):
        if not self._is_valid(addr):
            raise ValueError("Not a valid MAC address")
        
        # Normalize the address by removing separators and converting to uppercase
        self._addr = addr.upper().replace(":", "").replace("-", "")

        # Store the address as a list of 2-character segments for immutability
        self._segments = [self._addr[i:i+2] for i in range(0, 12, 2)]

    def _is_valid(self, addr: str) -> bool:
        return bool(self._regex.match(addr))

    def __getitem__(self, index):
        return self._segments[index]

    def __len__(self):
        return len(self._segments)

    def __repr__(self):
        return self.formatted('')

    def formatted(self, separator=':'):
        # Join the segments with the specified separator
        return separator.join(self._segments)


class Command:
    
    _input_data = {}

    def __init__(self, _type, _spec, *args, **kwargs):
        self._type = _type
        self._spec = _spec
        self._transform(*args, **kwargs)

    def __str__(self) -> str: return self.to_xml()
    def __repr__(self): return self.to_xml()
    def _transform(self, *args, **kwargs):
        """Transform input to dictionary based on command spec"""
        if args:
            attribute_keys = list(self._spec.get('attributes', {}).keys())
            element_keys = list(self._spec.get('elements', {}).keys())
            self._input_data.update(zip(attribute_keys + element_keys, args))

        cleaned_kwargs = {
            k.upper(): v if not isinstance(v, dict) else {sk.upper(): sv for sk, sv in v.items()}
            for k, v in kwargs.items()
        }
        self._input_data.update(cleaned_kwargs)
        


    def validate(self):
        for key, spec in self._spec.get('attributes', {}).items():
            if spec['required'] and key not in self._input_data:
                raise ValueError(f"Attribute {key} is required for {self._type}")
            if key in self._input_data:
                self._validate_value(key, spec)

        for key, spec in self._spec.get('elements', {}).items():
            if spec['required'] and key not in self._input_data:
                raise ValueError(f"Element {key} is required for {self._type}")
            if key in self._input_data:
                self._validate_value(key, spec, is_element=True)

    def _validate_value(self, key, spec, is_element=False):
        value = self._input_data[key]
        try:
            if is_element and isinstance(value, dict):
                element_value = value.get('VALUE', '')
                value['VALUE'] = spec['type'](element_value)
                if 'attributes' in spec:
                    for attr_key, attr_spec in spec['attributes'].items():
                        if attr_key in value:
                            value[attr_key] = attr_spec['type'](value[attr_key])
            else:
                self._input_data[key] = spec['type'](value)
        except (TypeError, ValueError) as e:
            raise TypeError(f"{key}: {str(e)}")

    def to_xml(self):
        self.validate()
        usg_dict = { '@COMMAND': self._type }
        for key in self._spec.get('attributes', {}):
            if key in self._input_data:
                usg_dict[f'@{key}'] = str(self._input_data[key])
        for key in self._spec.get('elements', {}):
            if key in self._input_data:
                element_value = self._input_data[key]
                if isinstance(element_value, dict):
                    element_dict = {'#text': str(element_value.pop('VALUE', ''))}
                    for attr_key, attr_value in element_value.items():
                        element_dict[f'@{attr_key}'] = str(attr_value)
                    usg_dict[key] = element_dict
                else:
                    usg_dict[key] = str(element_value)
        return xmltodict.unparse({'USG': usg_dict}, pretty=True)

    def help(self):
        """Generate help text for the command."""
        help_text = f"Help for {self._type}:\n"
        
        if 'attributes' in self._spec:
            help_text += "\nAttributes:\n"
            for key, spec in self._spec['attributes'].items():
                if key == 'COMMAND':
                    continue
                help_text += f"  {key}: "
                if 'help_text' in spec:
                    help_text += f"{spec['help_text']}\n"
                else:
                    help_text += f"Type: {spec['type'].__name__}, Required: {spec['required']}\n"
        if 'elements' in self._spec:
            help_text += "\nElements:\n"
            for key, spec in self._spec['elements'].items():
                help_text += f"  {key}: "
                if 'help_text' in spec:
                    help_text += f"{spec['help_text']}\n"
                else:
                    help_text += f"Type: {spec['type'].__name__}, Required: {spec['required']}\n"
        
        return help_text