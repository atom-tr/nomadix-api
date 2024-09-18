# -*- coding: UTF-8 -*-
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


class Command:
    def __init__(self, command_type, command_spec, **kwargs):
        self.command_type = command_type
        self.command_spec = command_spec
        self.kwargs = {k.upper(): v if not isinstance(v, dict) else {sk.upper(): sv for sk, sv in v.items()} for k, v in kwargs.items()}
        self.kwargs['COMMAND'] = command_spec['attributes']['COMMAND']

    def validate(self):
        for key, spec in self.command_spec['attributes'].items():
            if key == 'COMMAND':
                continue
            if spec['required'] and key not in self.kwargs:
                raise ValueError(f"Attribute {key} is required for {self.command_type}")
            if key in self.kwargs:
                value = self.kwargs[key]
                try:
                    self.kwargs[key] = spec['type'](value)
                except (TypeError, ValueError) as e:
                    raise TypeError(f"Attribute {key}: {str(e)}")
        if 'elements' in self.command_spec:
            for key, spec in self.command_spec['elements'].items():
                if spec['required'] and key not in self.kwargs:
                    raise ValueError(f"Element {key} is required for {self.command_type}")
                if key in self.kwargs:
                    value = self.kwargs[key]
                    if isinstance(value, dict):
                        # Handle element with attributes
                        element_value = value.get('VALUE', '')
                        try:
                            value['VALUE'] = spec['type'](element_value)
                        except (TypeError, ValueError) as e:
                            raise TypeError(f"Element {key}: {str(e)}")
                        
                        # Validate attributes if specified in the spec
                        if 'attributes' in spec:
                            for attr_key, attr_spec in spec['attributes'].items():
                                if attr_key in value:
                                    try:
                                        value[attr_key] = attr_spec['type'](value[attr_key])
                                    except (TypeError, ValueError) as e:
                                        raise TypeError(f"Element {key}, Attribute {attr_key}: {str(e)}")
                    else:
                        # Handle element without attributes
                        try:
                            self.kwargs[key] = spec['type'](value)
                        except (TypeError, ValueError) as e:
                            raise TypeError(f"Element {key}: {str(e)}")

    def to_xml(self):
        self.validate()
        
        usg_dict = {}
        for key in self.command_spec['attributes']:
            if key in self.kwargs:
                usg_dict[f'@{key}'] = str(self.kwargs[key])
        if 'elements' in self.command_spec:
            for key in self.command_spec['elements']:
                if key in self.kwargs:
                    element_value = self.kwargs[key]
                    if isinstance(element_value, dict):
                        # If the element has attributes
                        element_dict = {'#text': str(element_value.pop('VALUE', ''))}
                        for attr_key, attr_value in element_value.items():
                            element_dict[f'@{attr_key}'] = str(attr_value)
                        usg_dict[key] = element_dict
                    else:
                        # If the element doesn't have attributes
                        usg_dict[key] = str(element_value)
        
        return xmltodict.unparse({'USG': usg_dict}, pretty=True)

    def help(self):
        """Generate help text for the command."""
        help_text = f"Help for {self.command_type}:\n\n"
        
        help_text += "Attributes:\n"
        for key, spec in self.command_spec['attributes'].items():
            if key == 'COMMAND':
                continue
            help_text += f"  {key}: "
            if 'help_text' in spec:
                help_text += f"{spec['help_text']}\n"
            else:
                help_text += f"Type: {spec['type'].__name__}, Required: {spec['required']}\n"
        
        help_text += "\nElements:\n"
        for key, spec in self.command_spec['elements'].items():
            help_text += f"  {key}: "
            if 'help_text' in spec:
                help_text += f"{spec['help_text']}\n"
            else:
                help_text += f"Type: {spec['type'].__name__}, Required: {spec['required']}\n"
        
        return help_text