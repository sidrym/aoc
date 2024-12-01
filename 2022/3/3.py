#lang python

with open("input.txt") as f:
    count = 0
    for line in f:
        s1, s2 = line[:len(line)//2], line[len(line)//2:]
        for i in s1:
            if i in s2:
                i = ord(i)
                if i > 96:
                    count += i - 96
                else:
                    count += i - 38
                break
    print(count)
