#lang python
file = 'input.txt'
import re, collections

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

line = [int(i) for i in f[0]]
ans = []
nums, spaces = collections.deque(), collections.deque()

i = 0
while i < len(line):
	nums.append([i//2] * line[i])
	i += 1
	if i != len(line):
		spaces.append(line[i])
		i += 1

while spaces and nums:
	good_node = nums.popleft()
	ans.extend(good_node)
	while spaces[0] > 0 and nums:
		if len(nums[-1]) == 0:
			nums.pop()
		if nums:
			ans.append(nums[-1].pop())
		spaces[0] -= 1
	spaces.popleft()

for i, num in enumerate(ans):
	silver += num*i

## part 2
nums = []
i = 0
while i < len(line):
	nums.append([i//2] * line[i])
	i += 1
	if i != len(line):
		nums.append(["S", line[i]])
		i += 1

finalans = []
visited = set()
for _ in range(100000):
	flag = False
	for i in range(len(nums)-1, -1, -1):
		if nums[i][0] in visited:
			continue
		if nums[i][0] != 'S':
			for blank_idx in range(len(nums)):
				if blank_idx < i and nums[blank_idx][0] == 'S' and nums[blank_idx][1] >= len(nums[i]):
					pop = nums[i]
					nums[i] = ['S', len(pop)]
					nums[blank_idx][1] -= len(pop)
					nums.insert(blank_idx, pop)
					flag = True
					break
		if flag:
			break
		else:
			visited.add(nums[i][0])

	newnums = [nums.pop(0)]
	for num in nums:
		if newnums[-1] == ['S', 0]:
			newnums.pop()
		if newnums[-1][0] == 'S' and num[0] == 'S':
			newnums[-1][1] += num[1]
		else:
			newnums.append(num)

	nums = newnums

i = 0
while nums:
	top = nums.pop(0)
	if top[0] == 'S':
		i += top[1]
	else:
		while top:
			gold += i * top.pop(0)
			i += 1

print("silver", silver)
print("gold", gold)


