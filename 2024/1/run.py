#lang python
file = 'input.txt'

import collections
f = [i.strip() for i in open(file).readlines()]

l1, l2 = [], []
counter = collections.defaultdict(int)

for line in f:
	l = line.split()
	l1.append(int(l[0]))
	l2.append(int(l[-1]))

	counter[int(l[1])] += 1

l1.sort()
l2.sort()


print("silver:", sum(abs(l1[i]-l2[i]) for i in range(len(l1))))
print("gold:", sum(n * counter[n] for n in l1))


