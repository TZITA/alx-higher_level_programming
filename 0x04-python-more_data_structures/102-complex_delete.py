#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = {key: val for key, val in a_dictionary.items() if val != value}
    return new
