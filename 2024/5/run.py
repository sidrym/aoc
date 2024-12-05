#lang python
file = 'input.txt'
import collections

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

updates = []
prereq_map = collections.defaultdict(set)

c = 0
while f[c] != '':
	one, req = [int(i) for i in f[c].split('|')]
	prereq_map[one].add(req)
	c += 1
c += 1

def check_update(update):
	orig = update.copy()
	flag = True
	while flag:
		flag = False
		for i in range(len(update)):
			if update[i] in prereq_map:
				for after_page in prereq_map[update[i]]:
					if after_page in update:
						if update.index(after_page) < i:
							popped = update.pop(update.index(after_page))
							update.insert(i+1, popped)
							flag = True
	if update == orig:
		return []
	else:
		return update

while c < len(f):
	update = [int(i) for i in f[c].split(',')]
	res = check_update(update)
	if res == []:
		silver += update[len(update)//2]
	else:
		gold += res[len(res)//2]
	c += 1


print("silver", silver)
print("gold", gold)