include strutils
include sequtils

var sum = 0

for line in lines("input.txt"):
  let args = line.split(' ')
  let limits = args[0].split('-').mapIt(parseInt(it) - 1)
  let spec = args[1][0]
  if (args[2][limits[0]] == spec) xor (args[2][limits[1]] == spec):
    sum += 1

echo sum
