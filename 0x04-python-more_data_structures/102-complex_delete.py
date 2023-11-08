#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l = list(a_dictionary.keys())
    c = list(a_dictionary.values())
    for i in range(len(c)):
        if value == c[i]:
            word = l[i]
            del a_dictionary[word]
    return a_dictionary
