#!/usr/bin/python3
def weight_average(my_list=[]):
    new_list = []
    count = 0
    if len(my_list) == 0:
        return (0)
    for e in my_list:
        new_list.append(e[0] * e[1])
        count += e[1]
    return (sum(new_list) / count)
