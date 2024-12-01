#lang python
heatmap = [list(map(ord, list(i.strip()))) for i in open("input.txt")]

start = ()
end = ()
alist = []
for x in range(len(heatmap)):
	for y in range(len(heatmap[x])):
		if heatmap[x][y] == 83:
			start = (x, y)
			heatmap[x][y] = 0
		elif heatmap[x][y] == 69:
			end = (x, y)
			heatmap[x][y] = 26
		elif heatmap[x][y] == 97:
			alist.append((x,y))
			heatmap[x][y] -= 96
		else:
			heatmap[x][y] -= 96


def canvisit(x, y, visited):
	return 0<=x< len(heatmap) and 0<=y<len(heatmap[0]) and not visited[x][y]

def bfs(x, y):
	visited = [[False for _ in range(len(heatmap[0]))] for _ in range(len(heatmap))]
	queue = []
	queue.append((x, y, 0))
	visited[x][y] = True
	while len(queue) != 0:
		source = queue.pop(0)
		x, y, dist = source
		if (x, y) == end:
			return dist
		if canvisit(x-1, y, visited) and (heatmap[x-1][y] <= heatmap[x][y]+ 1):
			queue.append((x-1, y ,dist+1))
			visited[x-1][y] = True
		if canvisit(x+1, y, visited) and (heatmap[x+1][y] <= heatmap[x][y]+ 1):
			queue.append((x+1, y ,dist+1))
			visited[x+1][y] = True
		if canvisit(x, y-1, visited) and (heatmap[x][y-1] <= heatmap[x][y]+ 1):
			queue.append((x, y-1,dist+1))
			visited[x][y-1] = True
		if canvisit(x, y+1, visited) and (heatmap[x][y+1] <= heatmap[x][y]+ 1):
			queue.append((x, y+1,dist+1))
			visited[x][y+1] = True
	return -1

res = []
for i in alist:
	r = bfs(i[0],i[1])
	if r > 0:
		res.append(r)
print(min(res))
