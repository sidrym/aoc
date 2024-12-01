include sequtils

#289 too high
var args: seq[seq[string]]
let fields = @["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
let colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
let hair = ['a', 'b', 'c', 'd', 'e', 'f']
var sum = 0


for line in lines("input.txt"):
  if len(line) != 0:
    args.add(line.split(' ').mapIt(it.split(':')))
  else:
    var temp_fields = fields
    block temp:
      for pair in args:
        temp_fields.delete(temp_fields.find(pair[0]))
        case pair[0]:
          of "byr":
            if (pair[1].len != 4) or (pair[1].parseInt < 1920) or
            (pair[1].parseInt > 2002):
              break temp
          of "iyr":
            if (pair[1].len != 4) or (pair[1].parseInt < 2010) or
            (pair[1].parseInt > 2020):
              break temp
          of "eyr":
            if (pair[1].len != 4) or (pair[1].parseInt < 2020) or
            (pair[1].parseInt > 2030):
              break temp
          of "hgt":
            if pair[1].endsWith("cm"):
              var pair_temp = pair[1]
              pair_temp.removeSuffix("cm")
              let height = parseInt(pair_temp)
              if (height < 150) or (height > 193):
                break temp
            elif pair[1].endsWith("in"):
              var pair_temp = pair[1]
              pair_temp.removeSuffix("in")
              let height = parseInt(pair_temp)
              if (height < 59) or (height > 76):
                break temp
            else:
              break temp
          of "hcl":
             if pair[1][0] != '#':
               break temp
             else:
               var pair_temp = pair[1]
               removePrefix(pair_temp, '#')
               if pair_temp.len != 6:
                 break temp
               for c in pair_temp:
                 if (not hair.contains(c)) and (not isDigit(c)):
                   break temp
          of "ecl":
            if not colors.contains(pair[1]):
              break temp
          of "pid":
            if pair[1].len != 9:
              break temp
            else:
              try:
                discard pair[1].parseInt()
              except ValueError:
                break temp
          of "cid":
            discard
          else:
            break temp
      if temp_fields == @[] or temp_fields == @["cid"]:
        sum += 1
    args = @[]

echo sum
