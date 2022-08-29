#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    first_letter = sentence[0]
    if len_s == 0:
        first_letter = None
    return (len_s, first_letter)
