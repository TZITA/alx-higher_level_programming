#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        a = list(a_dictionary)
        for i in range(len(a_dictionary)):
            k, max_val = a[0], a_dictionary[a[0]]
            if a_dictionary[a[i]] > max_val:
                k, max_val = a[i], a_dictionary[a[i]]
        return k
