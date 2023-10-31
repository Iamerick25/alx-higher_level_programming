#!/usr/bin/python3
def uppercase(str):
    nstr = ''
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            nstr = nstr + chr(ord(str[i]) - 32)
        else:
            nstr = nstr + str[i]
    print("{}".format(nstr))
