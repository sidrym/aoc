#lang python
file = 'input.txt'
import re, collections, functools, itertools, sys, math

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

vowels = [i.strip() for i in f[0].strip().split(',')]

@functools.cache
def can_make_word(word, ans=0):
	if word == '':
		return 1
	for v in vowels:
		if word.startswith(v):
			ans += can_make_word(word[len(v):])
	return ans

f.pop(0)
f.pop(0)
while f:
	word = f.pop(0)
	if can_make_word(word):
		silver += 1
	gold += can_make_word(word)


print("silver", silver)
print("gold", gold)

