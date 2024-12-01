import strutils, sequtils

type Pos = tuple[x, y: int]

proc advance(code: char, wire: Pos): Pos =
  result = wire
  case code
  of 'U': result.y += 1
  of 'R': result.x += 1
  of 'L': result.x -= 1
  of 'D': result.y -= 1
  else: discard

var based: seq[seq[Pos]]
for wire in lines "input.txt":
  var point: Pos
  var current = wire.split(',')
  var points: seq[Pos]
  for instruction in current:
    let distance = parseInt(instruction[1..^1])
    let direction = instruction[0]
    for i in 1 .. distance:
      var point = advance(direction, point)
      points.add(point)
  based.add(points)

var max = int.high
for intersection in based[0].filterIt(it in based[1]):
  var manhattan = abs(intersection.x) + abs(intersection.y)
  if (manhattan < max):
    max = manhattan
echo max
