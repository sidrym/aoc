include strutils, sequtils

var pos = -3
var sum = 0

for line in lines("input.txt"):
  pos += 3
  pos = pos mod 31
  if line[pos] == '#':
    sum += 1

echo sum
