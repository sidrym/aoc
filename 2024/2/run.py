#lang python
file = 'input.txt'

import collections
f = [i.strip() for i in open(file).readlines()]

def check_line(l):
	if l[1] > l[0]:
		for i in range(1, len(l)):
			if (l[i] - l[i-1]) > 3 or (l[i] - l[i-1]) < 0 or (l[i] - l[i-1]) == 0:
				return False
	else:
		for i in range(1, len(l)):
			if (l[i] - l[i-1]) > 0 or (l[i] - l[i-1]) < -3 or (l[i] - l[i-1]) == 0:
				return False
	return True

silver = 0
gold = 0

for line in f:
	l = [int(i) for i in line.split()]

	silver_flag = True
	if check_line(l):
		silver += 1

	for remove_index in range(len(l)):
		l2 = l.copy()
		l2.pop(remove_index)
		
		if check_line(l2):
			gold += 1
			break

print("silver", silver)
print("gold", gold)
