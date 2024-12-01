import strutils

block main:
  for line1 in lines "input.txt":
    for line2 in lines "input.txt":
      if parseInt(line1) + parseInt(line2) == 2020:
        echo parseInt(line1) * parseInt(line2)
        break main
