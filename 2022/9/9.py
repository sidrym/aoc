#lang python

instr = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

lines = []
with open("input.txt") as f:
	for line in f:
		line = line.split()
		lines.append((line[0], int(line[1])))

headx, heady = 0, 0
tailx, taily = 0, 0
hist = {(0,0)}

for line in lines:
	for i in range(line[1]):
		headx += instr[line[0]][0]	
		heady += instr[line[0]][1]	
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
			hist.add((tailx, taily))
print(len(hist))
