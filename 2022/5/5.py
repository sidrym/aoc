#lang python

def manhattan(a, b, x, y):
	return abs(x - a) + abs(y - b)


#            [M] [S] [S]            
#        [M] [N] [L] [T] [Q]        
#[G]     [P] [C] [F] [G] [T]        
#[B]     [J] [D] [P] [V] [F] [F]    
#[D]     [D] [G] [C] [Z] [H] [B] [G]
#[C] [G] [Q] [L] [N] [D] [M] [D] [Q]
#[P] [V] [S] [S] [B] [B] [Z] [M] [C]
#[R] [H] [N] [P] [J] [Q] [B] [C] [F]
# 1   2   3   4   5   6   7   8   9 
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

		for i in range(amount):
			crates[dest].append(crates[src].pop())

	for i in crates:
		if i:
			print(i[-1], end='') 
