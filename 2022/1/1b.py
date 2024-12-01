#lang python

with open("input.txt") as f:
    count = 0
    res = []
    for line in f:
        if line == '\n':
            res.append(count)
            count = 0
        else:
            count += int(line)

    res.sort(reverse=True)
    print(res[0] + res[1] + res[2])
