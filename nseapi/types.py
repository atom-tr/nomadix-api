# -*- coding: UTF-8 -*-
from typing import Generic, TypeVar, List

T = TypeVar('T')

class FixedCharArray(Generic[T]):
    def __init__(self, size: int):
        self.size = size
        self.data: List[T] = [''] * size

    def set_value(self, input_string: str):
        if len(input_string) > self.size:
            raise ValueError(f"Input exceeds {self.size} characters")
        for i in range(len(input_string)):
            self.data[i] = input_string[i]

    def __str__(self):
        return ''.join(self.data).rstrip()

class CharArray(Generic[T]):
    def __init__(self, max_length: int = 96):
        self.max_length = max_length
        self.data: List[T] = []

    def add(self, char: T):
        if len(self.data) >= self.max_length:
            raise ValueError(f"Cannot add more characters, max length {self.max_length} reached.")
        if len(char) != 1:
            raise ValueError("Only single characters are allowed.")
        self.data.append(char)

    def set_value(self, input_string: str):
        if len(input_string) > self.max_length:
            raise ValueError(f"Input exceeds {self.max_length} characters.")
        self.data = list(input_string)

    def __str__(self):
        return ''.join(self.data)