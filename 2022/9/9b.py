#lang python

instr = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

lines = []
with open("input.txt") as f:
	for line in f:
		line = line.split()
		lines.append((line[0], int(line[1])))

rope = [(0,0)] * 10
headx, heady = 0, 0
tailx, taily = 0, 0
hist = set()

for line in lines:
	offset = instr[line[0]]
	for i in range(line[1]):
		headx, heady = rope[0]
		rope[0] = headx + offset[0], heady + offset[1]
		for i in range(1, len(rope)): 
			headx, heady = rope[0]
			headx, heady = rope[i-1]
			tailx, taily = rope[i]
			while max(abs(tailx - headx), abs(taily - heady)) > 1:
				if abs(tailx - headx) > 0:
					if headx > tailx:
						tailx += 1
					else:
						tailx -= 1
				if abs(taily - heady) > 0:
					if heady > taily:
						taily += 1
					else:
						taily -= 1
			rope[i] = tailx, taily
		hist.add(rope[-1])

print(len(hist))
