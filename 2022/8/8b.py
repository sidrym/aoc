#lang python

def is_visible(x, y):
	if x == 0 or x == len(trees)-1 or y == 0 or y == len(trees[0])-1:
		return 1
	ceil = trees[x][y]
	temp = x
	a = 0
	while True:
		a += 1
		temp -= 1
		if temp < 0 or trees[temp][y] >= ceil:
			break

		if temp == 0:
			break

	temp = x
	b = 0
	while True:
		b += 1
		temp += 1
		if temp >= len(trees) or trees[temp][y] >= ceil:
			break
		if temp == len(trees)-1:
			break

	temp = y
	c = 0
	while True:
		c += 1
		temp -= 1
		if temp < 0 or trees[x][temp] >= ceil:
			break

		if temp == 0:
			break

	temp = y
	d = 0
	while True:
		d += 1
		temp += 1
		if temp >= len(trees[0]) or trees[x][temp] >= ceil:
			break
		if temp == len(trees[0])-1:
			break

	return a * b * c * d

trees = []
with open("input.txt") as f:
	for line in f:
		trees.append([int(i) for i in line.strip()])
	result = 0

	for x in range(len(trees)):
		for y in range(len(trees[0])):
			result = max(result, is_visible(x, y))
	print(result)
	print(is_visible(3,2))