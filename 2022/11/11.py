#lang python
import math as math


monke_items = []
monke_op = []
monke_test = []
with open("input.txt") as f:
	f.readline()
	while True:
		monke_items.append([int(i) for i in f.readline().strip().replace(',', '').split( )[2:]])
		monke_op.append(f.readline().strip()[17:])
		test_local = []
		for i in range(3):
			test_local.append(int(f.readline().strip().split()[-1]))
		monke_test.append(test_local)
		f.readline()
		if f.readline() == '':
			break


inspects = [0 for i in range(len(monke_items))]
gcd = [1 for i in range(len(monke_items) + 1)]
for i in range(len(monke_items)):
	gcd.append(math.gcd(*monke_items[i]))
	for j in range(len(monke_items[i])):
		monke_items[i][j] = monke_items[i][j] / gcd[i]

for z in range(20):
	for monkey in range(len(monke_items)):
		for old in monke_items[monkey]:
			inspects[monkey] += 1
			old *= gcd[monkey]
			worry_level = int(eval(monke_op[monkey]) // 3)
			if worry_level % monke_test[monkey][0] == 0:
				monke_items[monke_test[monkey][1]].append(worry_level)
			else:
				monke_items[monke_test[monkey][2]].append(worry_level)
		monke_items[monkey] = []


inspects.sort()
print(inspects[-1] * inspects[-2])
