#lang python
import itertools

with open("input.txt") as f:
    count = 0
    hello = []
    while True:
        triple = list(map(str.strip, list(itertools.islice(f, 3))))
        if not triple:
            break
        hello.append(triple)

    for line in hello:
        for i in line[0]:
            if i in line[1] and i in line[2]:
                i = ord(i)
                if i > 96:
                    count += i - 96
                else:
                    count += i - 38
                break
    print(count)

                

