#!/usr/bin/python3
"""Defines a class MyInt."""


class MyInt(int):
    """A rebel class that inverts == with != and vice versa."""

    def __eq__(self, value):
        """Inverts == with !="""
        return self.real != value

    def __ne__(self, value):
        """Inverts != with =="""
        return self.real == value
