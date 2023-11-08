#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    return [replace if search == element else element for element in newlist]
