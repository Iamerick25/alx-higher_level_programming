#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = 0
if number < 0:
    i = -(-number % 10)
else:
    i = number % 10
print("Last digit of {} is {} and is ".format(number, i), end="")
if i > 5:
    print("greater than 5")
elif i == 0:
    print('0')
else:
    print('less than 6 and not 0')
