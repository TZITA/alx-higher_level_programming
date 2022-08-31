#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    else:
        tobeadded = []
        sum1 = 0
        for i in range(len(roman_string)):
            if roman_string[i] == "I":
                tobeadded.append(1)
            elif roman_string[i] == "V":
                if i > 0 and roman_string[i - 1] == "I":
                    tobeadded.append(3)
                else:
                    tobeadded.append(5)
            elif roman_string[i] == "X":
                if roman_string[i - 1] == "I":
                    tobeadded.append(8)
                else:
                    tobeadded.append(10)
            elif roman_string[i] == "L":
                tobeadded.append(50)
            elif roman_string[i] == "C":
                tobeadded.append(100)
            elif roman_string[i] == "D":
                tobeadded.append(500)
            elif roman_string[i] == "M":
                tobeadded.append(1000)
        for j in range(len(tobeadded)):
            sum1 += int(tobeadded[j])
        return sum1
