#lang python

crates = [['r', 'p', 'c', 'd', 'b', 'g'], 
['h', 'v', 'g'], 
['n', 's', 'q', 'd', 'j', 'p', 'm'], 
['p', 's', 'l', 'g', 'd', 'c', 'n', 'm'], 
['j', 'b', 'n', 'c', 'p', 'f', 'l', 's'], 
['q', 'b', 'd', 'z', 'v', 'g', 't', 's'], 
['b', 'z', 'm', 'h', 'f', 't', 'q'], 
['c', 'm', 'd', 'b', 'f'], 
['f', 'c', 'q', 'g']]

with open("input.txt") as f:
	for line in f:
		line = line.strip().split(' ')
		amount = int(line[1])
		src = int(line[3]) - 1
		dest = int(line[-1]) - 1

		newmove = crates[src][-amount:]
		crates[dest] += newmove
		for i in range(amount):
			crates[src].pop()


	for i in crates:
		if i:
			print(i[-1], end='') 
