#lang python
file = 'input.txt'
import re

f = [line.strip() for line in open(file).readlines()]
silver, gold = 0, 0

def dfs(target, nums, gold, acc=0):
	if not nums and acc == target:
		return True
	elif not nums:
		return False

	res = dfs(target, nums[1:], gold, acc+nums[0]) or dfs(target, nums[1:], gold, acc*nums[0])
	if gold:
		res = res or dfs(target, nums[1:], gold, int(str(acc) + str(nums[0])))
	return res

for i, line in enumerate(f):
	n = [int(i) for i in re.findall(r'\d+', line)]
	head, values = n[0], n[1:]
	if dfs(head, values, False):
		silver += head
	if dfs(head, values, True):
		gold += head


print("silver", silver)
print("gold", gold)

