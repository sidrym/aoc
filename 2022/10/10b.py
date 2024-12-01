#lang python
import itertools

x = 1
vals = []

with open("input.txt") as f:
	for line in f:
		line = line.strip().split()
		vals.append(0)
		if len(line) == 2:
			vals.append(int(line[1]))
	vals = itertools.accumulate(vals, initial=1)
	res = ''
	for i, value in enumerate(vals, 0):
		i %= 40
		res += '#' if i in range(value-1, value+2) else ' '
		if i == 0:
			print(res)
			res = ""
		i %= 40
