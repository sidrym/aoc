include strutils
include sequtils

var sum = 0

for line in lines("input.txt"):
  let args = line.split(' ')
  let limits = args[0].split('-').mapIt(parseInt(it))
  let spec = args[1][0]
  var i = 0
  for c in args[2]:
    if c == spec:
      i += 1
  if (i >= limits[0]) and (i <= limits[1]):
    sum += 1

echo sum
