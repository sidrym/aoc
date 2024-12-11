#lang python
import collections
file = 'input.txt'
import re, collections

f = [line.strip() for line in open(file).readlines()]

for i, line in enumerate(f):
	f[i] = [int(i) for i in line.strip()]

dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]
def bfs(node):
	queue = collections.deque()
	queue.append(node)
	seen = set()
	ans = 0
	while queue:
		node = queue.popleft()
		for d in dirs:
			nr, nc = node[0] + d[0], node[1] + d[1]
			if (nr, nc) not in seen and 0<=nr<len(f) and 0<=nc<len(f[0]) and f[node[0]][node[1]] == f[nr][nc]-1:
				if f[nr][nc] == 9:
					ans += 1
				else:
					queue.append((nr, nc))
				seen.add((nr, nc))
	return ans

def dfs(node):
	if f[node[0]][node[1]] == 9:
		return 1
	ans = 0
	for d in dirs:
		nr, nc = node[0] + d[0], node[1] + d[1]
		if 0<=nr<len(f) and 0<=nc<len(f[0]) and f[node[0]][node[1]] == f[nr][nc]-1:
			ans += dfs((nr, nc))
	return ans

gold, silver = 0, 0
for i in range(len(f)):
	for j in range(len(f[0])):
		if f[i][j] == 0:
			silver += bfs((i, j))
			gold += dfs((i, j))

print("silver", silver)
print("gold", gold)
