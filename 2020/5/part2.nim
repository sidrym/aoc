include sequtils

var seats: seq[int]

for line in lines("input.txt"):
  var id = line
  id = id.multiReplace(("F", "0"), ("B", "1"),
                       ("R", "1"), ("L", "0"))
  seats.add fromBin[int](id)

for seat in seats:
  if seat + 1 notin seats and
     seat + 2 in seats:
    echo seat + 1
