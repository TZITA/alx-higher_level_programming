#!/usr/bin/python3
"""Defines a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in a list of numbers"""
    if len(list_of_integers) == 0:
        return None
    else:
        set_l = set(list_of_integers)
        s_list = sorted(list(set_l))
        return s_list[len(s_list) - 1]
