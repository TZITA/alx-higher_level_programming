#!/usr/bin/python3
"""Defines a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in a list of numbers"""
    if len(list_of_integers) == 0:
        return None
    else:
        set_l = set(list_of_integers)
        list_a = list(set_l)
        peak = list_a[0]
        for i in range(1, len(list_a)):
            if list_a[i] > peak:
                peak = list_a[i]
        return peak
