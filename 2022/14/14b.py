#lang python
from PIL import Image

ceil = [850, 850]
start_point = (500, 0)
grid = [[0 for i in range(ceil[0])] for i in range (ceil[1])]
moves = [(0, 1), (-1, 1), (1, 1)]
frames = []
negative_ceil = 0

def add_img(rock):
	img = frames[-1].copy()
	pixels = img.load()
	pixels[rock[0]-300, rock[1]] = (255,255,0,255)
	img.crop((300, 0, 700, negative_ceil))
	frames.append(img)

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
		if start[1] > negative_ceil:
			negative_ceil = start[1]
		if end[1] > negative_ceil:
			negative_ceil = end[1]

		start = end

for i in range(0, 850):
	grid[i][negative_ceil+2] = 1

img = Image.new('RGB', (850, 850), (0, 0, 0))
pixels = img.load()
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if grid[i][j] == 1:
			pixels[i, j] = (255,255,255,255)
w, h = img.size
img = img.crop((300, 0, 700, negative_ceil))
frames.append(img)

counter = 0

while True:
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
	grid[rock[0]][rock[1]] = 2
	try:
		add_img(rock)
	except:
		pass
	counter += 1
	if rock == start_point:
		break
	print(counter)

frames[0].save('moving_ball.gif', format='GIF', append_images=frames[1:], save_all=True, duration=[0.05 for i in range(len(frames))], loop=1)
