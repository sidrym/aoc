#lang python

with open("input.txt") as f:
    ceil = 0
    count = 0
    for line in f:
        if line == '\n':
            if count > ceil:
                ceil = count
            count = 0
        else:
            count += int(line)

    print(ceil)
