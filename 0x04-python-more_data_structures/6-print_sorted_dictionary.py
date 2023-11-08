#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for words in sorted(a_dictionary.keys()):
        print("{}: {}".format(words, a_dictionary[words]))
