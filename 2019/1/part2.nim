import strutils

var sum = 0

for line in lines "input.txt":
  var local = 0
  var current = parseInt line
  while current > 0:
    current = current div 3 - 2
    if current > 0:
      local += current
  sum += local

echo sum
