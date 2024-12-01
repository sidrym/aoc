#lang python
# gave up for this one, need to implement myself later :( got close though
from functools import cmp_to_key
from math import prod

lines = [[*map(eval, i.split())] for i in open("input2.txt").read().split("\n\n")]

def compare(a, b):
	match(a, b):
		case int(), list(): return compare([a], b)
		case list(), int(): return compare(a, [b])
		case int(), int(): return (a>b)-(a<b)
		case list(), list():
			for i in map(compare, a, b):
				if i:
					return i
			return compare(len(a), len(b))
packets = [[*map(eval, x.split())] for x in open('input.txt').read().split('\n\n')]
print(sum(i for i, p in enumerate(packets, 1) if compare(*p) == -1))


packets = sorted(sum(packets, [[2], [6]]), key=cmp_to_key(compare))
print(prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]]))