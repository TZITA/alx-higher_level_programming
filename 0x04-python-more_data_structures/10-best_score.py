#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        lis = list(a_dictionary)
        max_val = a_dictionary[lis[0]]
        for k in lis:
            if a_dictionary[k] > max_val:
                max_val = a_dictionary[k]
        if max_val is None:
            return None
        else:
            key = {k for k, v in a_dictionary.items() if v == max_val}
            return list(key)[0]
