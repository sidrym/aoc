#lang python

x = 1
vals = []
queue = []


with open("input2.txt") as f:
	while True:
		vals.append(x)
		print(queue)
		for i in queue:
			if i: x += i.pop(0)
			else: queue.remove(i)
		if f:
			line = f.readline().strip().split()
			if line:
				if line[0] == 'addx':
					queue.append([0, 0, int(line[1])])
				else:
					queue.append([0])
		else:
			break
		trigger = 0
		for i in queue:
			if i:
				trigger = 1
		if not trigger:
			break

vals.append(x)
print(len(vals))
print(queue)
print(x)
print(vals)