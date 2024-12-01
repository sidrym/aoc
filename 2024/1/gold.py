#lang python
example = 'example.txt'

import collections

counter = collections.defaultdict(int)

f = [i.strip() for i in open(example).readlines()]
l1 = []
for line in f:
	l = line.split('   ')

	l1.append(int(l[0]))
	counter[int(l[1])] += 1

print(sum(n * counter[n] for n in l1))

