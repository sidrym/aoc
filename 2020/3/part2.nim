include strutils, sequtils

let incr = [1, 3, 5, 7, 1]

var
  pos = [-1, -3, -5, -7, -1]
  sum = [0, 0, 0, 0, 0]
  i = 0

for line in lines("input.txt"):
  i += 1
  var ite = (if i == 2: 3 else: 4)
  for j in countup(0, ite):
    pos[j] += incr[j]
    pos[j] = pos[j] mod 31
    if line[pos[j]] == '#':
      sum[j] += 1
  i = i mod 2

echo foldl(sum, a * b)
