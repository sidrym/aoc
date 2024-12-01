#lang python
from itertools import accumulate

with open("input.txt") as f:
	first = f.readline()
	current_path = ['/']
	directories = {}

	while True:
		line = f.readline().split()
		if not line:
			result = float('inf')
			for i in directories.values():
				if i >= directories['/'] - 40000000:
					if i <= result:
						result = i
			print(result)
			break

		command = line[1]
		current_dir = current_path[-1]
		if command == "cd":
			arg = line[2]
			if arg == "..":
				current_path.pop()
			elif arg == '/':
				current_path = ['/']
			else:
				current_path.append(arg)
		elif line[0].isnumeric():
			filesize = int(line[0])
			for i in accumulate(current_path):
				if not i i dnirectories:
					directories[i] = filesize
				else:
					directories[i] += filesize
