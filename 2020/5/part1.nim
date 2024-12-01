include sequtils, math

#931 too high

var start = [0, 127]
var highest = 0
var seats = @[int]

for line in lines("input.txt"):
  var start = [0, 127]
  for i in countup(0, 6):
    let rows = abs(start[1] - start[0])
    if line[i] == 'F':
      start[1] = start[0] + (int)ceil(rows/2)
    elif line[i] == 'B':
      start[0] = start[1] - (int)floor(rows/2)

  var row = (if line[8] == 'F': start[1] else: start[0])

  start = [0, 7]
  for i in countup(7, 9):
    let columns = abs start[1] - start[0]
    if line[i] == 'L':
      start[1] = start[0] + (int)ceil(columns/2)
    elif line[i] == 'R':
      start[0] = start[1] - (int)floor(columns/2)

  var column = (if line[9] == 'R': start[1] else: start[0])

  var id = (row * 8) + column
  if id > highest:
    highest = id

echo highest
