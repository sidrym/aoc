#lang python

def is_visible(x, y):
	if x == 0 or x == len(trees)-1 or y == 0 or y == len(trees[0])-1:
		return 1
	ceil = trees[x][y]
	temp = x
	while True:
		temp -= 1
		if temp < 0 or trees[temp][y] >= ceil:
			break

		if temp == 0:
			return 1

	temp = x
	while True:
		temp += 1
		if temp >= len(trees) or trees[temp][y] >= ceil:
			break
		if temp == len(trees)-1:
			return 1

	temp = y
	while True:
		temp -= 1
		if temp < 0 or trees[x][temp] >= ceil:
			break

		if temp == 0:
			return 1

	temp = y
	while True:
		temp += 1
		if temp >= len(trees[0]) or trees[x][temp] >= ceil:
			break
		if temp == len(trees[0])-1:
			return 1
	return 0

trees = []
with open("input2.txt") as f:
	for line in f:
		trees.append([int(i) for i in line.strip()])
	result = 0

	for x in range(len(trees)):
		for y in range(len(trees[0])):
			result += is_visible(x, y)
	print(result)

