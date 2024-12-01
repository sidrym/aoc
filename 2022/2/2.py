#lang python

rock = 1
paper = 2
scissors = 3
lose = 'X'
draw = 'Y'
win = 'Z'


with open("input.txt") as f:
    count = 0
    for line in f:
        opponent = line[0]
        if opponent == 'A':
            opponent = rock
        elif opponent == 'B':
            opponent = paper
        elif opponent == 'C':
            opponent = scissors
        me = line[2]

        if opponent == rock:
            if me == lose:
                count += scissors
            elif me == draw:
                count += rock + 3
            else:
                count += paper + 6
        elif opponent == paper:
            if me == lose:
                count += rock
            elif me == draw:
                count += paper + 3
            else:
                count += scissors + 6
        else:
            if me == lose:
                count += paper
            elif me == draw:
                count += scissors + 3
            else:
                count += rock + 6


    print(count)

