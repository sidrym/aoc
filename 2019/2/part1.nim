import strutils, sequtils

var nums: seq[int]

for line in lines "input.txt":
  nums.add line.split(',').map(parseInt)

nums[1] = 12
nums[2] = 2
for i in countup(0, nums.len, 4):
  if nums[i] == 1:
    nums[nums[i + 3]] = nums[nums[i + 1]] + nums[nums[i + 2]]
  elif nums[i] == 2:
    nums[nums[i + 3]] = nums[nums[i + 1]] * nums[nums[i + 2]]
  else:
    break

echo nums[0]
