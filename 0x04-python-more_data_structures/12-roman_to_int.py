#!/usr/bin/python3
def roman_to_int(roman_string):
    tobeadded = []
    sum1 = 0
    for i in range(len(roman_string)):
        if roman_string[i] =="I":
             tobeadded.append(1)
        elif roman_string[i] == "V":
             tobeadded.append(5)
        elif roman_string[i] == "X":
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
