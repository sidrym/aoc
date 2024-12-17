#lang python
file = 'input.txt'
import re, collections, functools, itertools, sys, math

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

def find_num(line):
	return [int(i) for i in re.findall(r'\d+', line)]

def find_min(a, b, prize):
	b_p = (a[1] * prize[0] - a[0] * prize[1]) / (a[1] * b[0] - a[0] * b[1])
	a_p = (prize[0] - b[0] * b_p) / a[0]
	if a_p.is_integer() and b_p.is_integer():
		return int(a_p * 3 + b_p)
	else:
		return 0
while f:
	a = find_num(f.pop(0))
	b = find_num(f.pop(0))
	prize = find_num(f.pop(0))
	silver += find_min(a, b, prize)
	gold += find_min(a, b, (prize[0]+10000000000000, prize[1] + 10000000000000))

	if f:
		f.pop(0)


print("silver", silver)
print("gold", gold)