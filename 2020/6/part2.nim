include sequtils

var
  sum = 0
  entries: seq[string]

for line in lines("input.txt"):
  if len(line) != 0:
    entries.add line
  else:
    for c in entries[0]:
      block temp:
        for entry in entries:
          if c notin entry:
            break temp
        sum += 1
    entries = @[]

echo sum
