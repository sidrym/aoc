#lang python
file = 'input.txt'
import re, collections, functools, itertools, sys, math

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

vowels = [i.strip() for i in f[0].strip().split(',')]
def find_num(line):
	return [int(i) for i in re.findall(r'-?\d+', line)]
def print_grid(g):
	for r, line in enumerate(g):
		print("".join(line))

size = 70
grid = [['.'] * (size+1) for _ in range(size+1)]
dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]

def bfs():
	queue = collections.deque()
	queue.append((0,0))
	seen = set()
	level = 0
	while queue:
		ceil = len(queue)
		level += 1
		for _ in range(ceil):
			node = queue.popleft()
			for d in dirs:
				nr, nc = node[0] + d[0], node[1] + d[1]
				if (nr, nc) == (size, size):
					return level
				if (nr, nc) not in seen and 0<=nr<(size+1) and 0<=nc<(size+1) and grid[nr][nc] == '.':
					queue.append((nr, nc))
					seen.add((nr, nc))
	return False

byte_count = 1024
for i, line in enumerate(f):
	r, c = find_num(line)
	grid[c][r] = '#'
	if not gold and not bfs():
		gold = (r, c)
	if i == byte_count:
		silver = bfs()
	if gold and silver:
		break

print("silver", silver)
print("gold", gold)

