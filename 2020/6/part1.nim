include sequtils

#

var entries: seq[char]
var sum: int

for line in lines("input.txt"):
  if len(line) != 0:
    for c in line:
      entries.add c
  else:
    sum += deduplicate(entries).len
    entries = @[]

sum += deduplicate(entries).len
echo sum
