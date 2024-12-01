include sequtils

var args: seq[string]
let fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
var sum = 0

for line in lines("input.txt"):
  if len(line) == 0:
    block temp:
      if args.len == 8:
        sum += 1
      elif args.len == 7:
        for arg in fields:
          if not args.contains(arg) and arg != "cid":
            break temp
        sum += 1
    args = @[]
  else:
    args.add line.split(' ').mapIt(it.split(':')[0])

echo sum
