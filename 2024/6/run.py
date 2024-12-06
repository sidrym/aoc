#lang python
file = 'input.txt'

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

dirs = ['v', '<', '^', '>']

guard, guard_symbol = [], ""
for i, line in enumerate(f):
	for d in dirs:
		if d in line:
			guard = [i, line.index(d)]
			guard_symbol = d
			break
	if guard: break

path = set()
def try_fail(x, y, guard, guard_symbol, f, silver):
	f[x] = f[x][:y] + '#' + f[x][y:][1:]

	i = 0
	# awful bruteforce
	while 0 < guard[0] < len(f)-1 and 0 < guard[1] < len(f[0])-1 and i < 10000:
		if silver:
			path.add((guard[0], guard[1]))
		if guard_symbol == 'v':
			if f[guard[0] + 1][guard[1]] != '#':
				guard[0] += 1
				i += 1
			else:
				guard_symbol = '<'
		elif guard_symbol == '<':
			if f[guard[0]][guard[1] - 1] != '#':
				guard[1] -= 1
				i += 1
			else:
				guard_symbol = '^'
		elif guard_symbol == '^':
			if f[guard[0] - 1][guard[1]] != '#':
				guard[0] -= 1
				i += 1
			else:
				guard_symbol = '>'
		elif guard_symbol == '>':
			if f[guard[0]][guard[1] + 1] != '#':
				guard[1] += 1
				i += 1
			else:
				guard_symbol = 'v'
	return i

try_fail(guard[0], guard[1], guard.copy(), guard_symbol, f.copy(), True)

for (x, y) in path:
	if try_fail(x, y, guard.copy(), guard_symbol, f.copy(), False) == 10000:
		gold += 1

print("silver", len(path)+1)
print("gold", gold+1)
