#lang python
file = 'input.txt'
import re, collections, functools, itertools, sys, math

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

def find_num(line):
	return [int(i) for i in re.findall(r'-?\d+', line)]

robots = []
speeds = []
for line in f:
	rob_x, rob_y, speed_x, speed_y = find_num(line)
	robots.append([rob_y, rob_x])
	speeds.append([speed_x, speed_y])

tiles_h = 103
tiles_w = 101

robots_copy = []
for z in range(10000):
	grid = [['.'] * tiles_w for _ in range(tiles_h)]
	if z == 100:
		robots_copy = robots.copy()
	for i in range(len(robots)):
		x = robots[i][0] + speeds[i][1]
		if x < 0:
			x += tiles_h
		else:
			x %= tiles_h
		y = robots[i][1] + speeds[i][0]
		if y < 0:
			y += tiles_w
		else:
			y %= tiles_w
		robots[i] = [x, y]
		grid[x][y] = '#'
	if gold == 0:
		for line in grid:
			if '############' in "".join(line):
				gold = z + 1
				break
				
fin = [[0, 0], [0, 0]]
count = collections.defaultdict(int)
for r in robots_copy:
	count[tuple(r)] += 1
grid = [['.'] * tiles_w for _ in range(tiles_h)]
for (x, y), amount in count.items():
	nx, ny = -1, -1
	if x < tiles_h // 2:
		nx = 0
	elif x > tiles_h // 2:
		nx = 1
	if y < tiles_w // 2:
		ny = 0
	elif y > tiles_w // 2:
		ny = 1
	if nx != -1 and ny != -1:
		fin[nx][ny] += amount
silver = fin[0][0] * fin[0][1] * fin[1][0] * fin[1][1]

print("silver", silver)
print("gold", gold)

