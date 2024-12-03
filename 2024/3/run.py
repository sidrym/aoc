#lang python
file = 'input.txt'

f = [i.strip() for i in open(file).readlines()]

silver = 0
gold = 0
do = True

for line in f:
	i = 0
	while i < len(line):
		if line[i:].startswith('mul('):
			i += 4
			j = i
			while line[j] != ')' and j <= len(line):
				j += 1
			nums_pair = line[i:j].split(',')
			if len(nums_pair) == 2 and nums_pair[0].isnumeric() and nums_pair[1].isnumeric():
				product = int(nums_pair[0]) * int(nums_pair[1])
				silver += product
				if do:
					gold += product
		elif line[i:].startswith('do()'):
			i += 4
			do = True
		elif line[i:].startswith("don't()"):
			i += 7
			do = False
		else:
			i += 1


print("silver", silver)
print("gold", gold)
