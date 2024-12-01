#lang python

with open("input.txt") as f:
	i = 0
	word = []
	while True:
		if len(word) > 14:
			word.pop(0)
		if len(set(word)) == 14:
				print(i)
				break
		c = f.read(1)
		if not c:
			break
		word.append(c)
		i += 1




