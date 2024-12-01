#lang python
example = 'example.txt'

f = [i.strip() for i in open(example).readlines()]
l1, l2 = [], []
for line in f:
	l = line.split('   ')
	l1.append(int(l[0]))
	l2.append(int(l[-1]))

l1.sort()
l2.sort()

ans = 0
for i in range(len(l1)):
	ans += abs(l1[i] - l2[i])

print(ans)

