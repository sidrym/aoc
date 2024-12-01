#lang python

with open("input.txt") as f:
    result = 0
    for line in f:
        line = line.strip().split(",")
        line = list(map(lambda n: n.split("-"), line))
        line = list(map(lambda n: list(map(lambda m: int(m), n)), line))
        first = line[0]
        second = line[1]
        if first[0] >= second[0] and first[1] <= second[1]:
            result += 1
        elif second[0] >= first[0] and second[1] <= first[1]:
            result += 1


    print(result)


