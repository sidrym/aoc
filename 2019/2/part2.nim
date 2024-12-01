import strutils, sequtils

var nums: seq[int]

for line in lines "input.txt":
  nums.add line.split(',').map(parseInt)

proc calculate(noun: int, verb: int): int =
  var local = nums
  local[1] = noun
  local[2] = verb
  for i in countup(0, local.len, 4):
    if local[i] == 1:
      local[local[i + 3]] = local[local[i + 1]] + local[local[i + 2]]
    elif local[i] == 2:
      local[local[i + 3]] = local[local[i + 1]] * local[local[i + 2]]
    else:
      break
  return local[0]

for noun in 0 .. 99:
  for verb in 0 .. 99:
    if calculate(noun, verb) == 19690720:
      echo 100 * noun + verb
