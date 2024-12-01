#lang python

with open("input.txt") as f:
    result = 0
    for line in f:
        a, b, c, d = [int(i) for i in line.strip().replace('-', ',').split(",")]

        if (a >= c and a <= d) or (b >= c and b <= c) or \
                (c >= a and c <= b) or (d >= a and d <= a):
            result += 1

    print(result)


