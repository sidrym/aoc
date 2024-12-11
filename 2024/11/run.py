#lang python
file = 'input.txt'
import re, collections, functools, itertools

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

@functools.cache
def calc_stone(stone, i):
	if i == 0:
		return 1
	if stone == 0:
		return calc_stone(1, i-1)
	elif len(str(stone)) % 2 == 0:
		return calc_stone(int(str(stone)[:len(str(stone))//2]), i-1) + calc_stone(int(str(stone)[len(str(stone))//2:]), i-1)
	return calc_stone(stone * 2024, i-1)

stones = [int(i) for i in re.findall(r'\d+', f[0])]
silver = sum([calc_stone(x, 25) for x in stones])
gold = sum([calc_stone(x, 75) for x in stones])

print("silver", silver)
print("gold", gold)



