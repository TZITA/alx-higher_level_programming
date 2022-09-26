#!/usr/bin/python3
"""Defines a class MyList."""


class MyList(list):
    """MyLits class that inherits from list object."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
