#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    c = list(a_dictionary.keys())
    for i in range(0, len(a_dictionary)):
        word = c[i]
        new_dict[word] = a_dictionary.get(word) * 2
    return new_dict
