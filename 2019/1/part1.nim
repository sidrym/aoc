import strutils

var sum = 0

for line in lines "input.txt":
  sum += parseInt(line) div 3 - 2

echo sum
