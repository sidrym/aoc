#lang python
heatmap = [list(map(ord, list(i.strip()))) for i in open("input.txt")]

start = ()
end = ()
for x in range(len(heatmap)):
	for y in range(len(heatmap[x])):
		if heatmap[x][y] == 83:
			start = (x, y)
			heatmap[x][y] = 0
		elif heatmap[x][y] == 69:
			end = (x, y)
			heatmap[x][y] = 26
		else:
			heatmap[x][y] -= 96

visited = [[False for _ in range(len(heatmap[0]))] for _ in range(len(heatmap))]

def canvisit(x, y):
	return 0<=x< len(heatmap) and 0<=y<len(heatmap[0]) and not visited[x][y]

def bfs():
	queue = []
	queue.append((start[0], start[1], 0))
	visited[start[0]][start[1]] = True
	while len(queue) != 0:
		source = queue.pop(0)
		x, y, dist = source
		if (x, y) == end:
			return dist
		if canvisit(x-1, y) and (heatmap[x-1][y] <= heatmap[x][y]+ 1):
			queue.append((x-1, y ,dist+1))
			visited[x-1][y] = True
		if canvisit(x+1, y) and (heatmap[x+1][y] <= heatmap[x][y]+ 1):
			queue.append((x+1, y ,dist+1))
			visited[x+1][y] = True
		if canvisit(x, y-1) and (heatmap[x][y-1] <= heatmap[x][y]+ 1):
			queue.append((x, y-1,dist+1))
			visited[x][y-1] = True
		if canvisit(x, y+1) and (heatmap[x][y+1] <= heatmap[x][y]+ 1):
			queue.append((x, y+1,dist+1))
			visited[x][y+1] = True
	return -1

print(bfs())
