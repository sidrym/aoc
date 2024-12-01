include sequtils, tables

# 8417 too high

let ender = " bags contain no other bags."

type bags = tuple
  amount: int
  value: string

var storage = initTable[string, seq[bags]]()
for line in lines("input.txt"):
  var newLine = line
  var bag: bags
  if line.endsWith(ender):
    newLine.removeSuffix(ender)
    storage[newLine] = @[]
    bag = (amount: 0, value: "")
    storage[newLine].add(bag)
  else:
    var words = line.split(' ')
    var key = words[0] & ' ' & words[1]
    newLine.removePrefix(key)
    newLine.removePrefix(" bags contain ")
    words = newLine.split(", ")
    var test = words.mapit(splitWhitespace(it))
    storage[key] = @[]
    for entry in test:
      bag = (amount: entry[0].parseInt, value: entry[1] & ' ' & entry[2])
      storage[key].add(bag)


proc recur(key: string): int =
  if storage[key][0][0] == 0:
    return 0
  else:
    for i in storage[key]:
      result += i[0] + i[0] * recur(i[1])

echo recur("shiny gold")
