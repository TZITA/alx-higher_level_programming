#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s == 0:
        return (len_s, None)
    else:
        first_letter = sentence[0]
        return (len_s, first_letter)
