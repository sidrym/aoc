#lang python
from PIL import Image

ceil = [600, 600]
start_point = (500, 0)
grid = [[0 for i in range(ceil[0])] for i in range (ceil[1])]
moves = [(0, 1), (-1, 1), (1, 1)]

def abyss(rock):
	return(true)

for i in open("input.txt"):
	i = [eval(j) for j in i.strip().split(' -> ')]

	start = []
	while i:
		if not start:
			start = i.pop(0)
		end = i.pop(0)

		if start[0] == end[0]:
			if start[1] < end[1]:
				for j in range(start[1], end[1]+1):
					grid[start[0]][j] = 1
			else:
				for j in range(start[1], end[1]-1, -1):
					grid[start[0]][j] = 1
		else:
			if start[0] < end[0]:
				for j in range(start[0], end[0]+1):
					grid[j][end[1]] = 1
			else:
				for j in range(start[0], end[0]-1, -1):
					grid[j][start[1]] = 1
		start = end

counter = 0

for i in range(0,100000):
	rock = start_point
	newflag = 1

	while newflag:
		newflag = 0
		for move in moves:
			x, y = rock[0]+move[0], rock[1]+move[1]
			try:
				if grid[x][y] == 0:
					newflag = 1
					rock = (x, y)
					break
			except:
				break

	if rock[1] > 500:
		break
	grid[rock[0]][rock[1]] = 2
	print(rock)
	counter += 1

print(counter)

img = Image.new('RGB', (600, 600), (0, 0, 0))
pixels = img.load()
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if grid[i][j] == 1:
			pixels[i, j] = (255,255,255,255)
		if grid[i][j] == 2:
			pixels[i,j] = (227,207,87)		
img.show()
