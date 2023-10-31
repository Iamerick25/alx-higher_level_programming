#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i + 1, 10):
        if i != 0 or n != 1:
            print(", {:02d}".format(i * 10 + n), end="")
        else:
            print("{:02d}".format(i * 10 + n), end="")
print()
