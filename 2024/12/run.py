#lang python
file = 'input.txt'
import re, collections, functools, itertools, sys

f = [list(line.strip()) for line in open(file).readlines()]
silver, gold = 0, 0
dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]

def bfs(node, letter):
	result = set()
	result.add(node)
	queue = collections.deque()
	queue.append(node)
	seen = set()
	while queue:
		node = queue.popleft()
		for d in dirs:
			nr, nc = node[0] + d[0], node[1] + d[1]
			if (nr, nc) not in seen and 0<=nr<len(f) and 0<=nc<len(f[0]):
				if f[nr][nc] == letter:
					f[nr][nc] = 0
					result.add((nr,nc))
					queue.append((nr, nc))
				seen.add((nr, nc))
	return result

def find_num(line):
	return [int(i) for i in re.findall(r'\d+', line)]

def calc_perimiter(nodes):
	ans = 0
	for node in nodes:
		p = 4
		for d in dirs:
			if (node[0] + d[0], node[1] + d[1]) in nodes:
				p -= 1
		ans += p
	return(ans)

corners = [[(-1,0), (-1,-1), (0, -1)], [(-1, 0), (-1, 1), (0, 1)], [(0, 1), (1, 1), (1, 0)], [(1, 0), (1, -1), (0, -1)]]
def calc_corners(char, nodes):
	result = 0

	for node in nodes:
		for corner_list in corners:
			adj1 = (node[0] + corner_list[0][0], node[1] + corner_list[0][1])
			adj2 = (node[0] + corner_list[2][0], node[1] + corner_list[2][1])
			diag = (node[0] + corner_list[1][0], node[1] + corner_list[1][1])

			if adj1 in nodes and adj2 in nodes and diag not in nodes:
				result += 1

			elif adj1 not in nodes and adj2 not in nodes and diag not in nodes:
				result += 1
			elif diag in nodes and adj1 not in nodes and adj2 not in nodes:
				result += 1

	return result

dic = {}
for r, line in enumerate(f):
	for c, char in enumerate(line):
		if char != 0:
			nodes = bfs((r,c), char)
			silver += len(nodes) * calc_perimiter(nodes)
			gold += len(nodes) * calc_corners(char, nodes)



print("silver", silver)
print("gold", gold)
