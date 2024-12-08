#lang python
file = 'input.txt'
import re, collections

f = [line.strip() for line in open(file).readlines()]

dic = collections.defaultdict(list)

for i, line in enumerate(f):
	for j in range(len(f[0])):
		if f[i][j] != '.':
			dic[f[i][j]].append((i,j))

diffs = collections.defaultdict(list)
antinodes_gold = set()
antinodes = set()
for freq, pairs in dic.items():
	for i in range(len(pairs)):
		for j in range(len(pairs)):
			if i == j:
				continue

			x1, y1 = pairs[i]
			x2, y2 = pairs[j]
			dx, dy = x2-x1, y2-y1
			node2 = (x2 + dx, y2 + dy)

			if 0 <= node2[0] < len(f) and 0 <= node2[1] < len(f[0]):
				antinodes.add(node2)

			antinodes_gold.add(pairs[i])
			antinodes_gold.add(pairs[j])
			while 0 <= node2[0] < len(f) and 0 <= node2[1] < len(f[0]):
				antinodes_gold.add(node2)
				node2 = (node2[0] + dx, node2[1] + dy)


print("silver", len(antinodes))
print("gold", len(antinodes_gold))

