#!/usr/bin/env python3

def getScore(s):
    scores = {'X':1,'Y':2,'Z':3}
    return scores[s]

def getResult(a,b):
    if a == 'A':
        if b == 'X':
            return 3
        elif b == 'Y':
            return 6
        elif b == 'Z':
            return 0
    elif a == 'B':
        if b == 'X':
            return 0
        elif b == 'Y':
            return 3
        elif b == 'Z':
            return 6
    elif a == 'C':
        if b == 'X':
            return 6
        elif b == 'Y':
            return 0
        elif b == 'Z':
            return 3

with open('Day2-input.txt','r') as f:
    lines = [_.rstrip().split(' ') for _ in f]

score = 0

for l in lines:
    score += getScore(l[1])
    score += getResult(l[0], l[1])

print('Part One -',score)

score = 0

for l in lines:
    match l[1]:
        case 'X':
            #Lose
            match l[0]:
                case 'A':
                    score += getScore('Z')
                case 'B':
                    score += getScore('X')
                case 'C':
                    score += getScore('Y')
        case 'Y':
            #Draw
            score += 3
            match l[0]:
                case 'A':
                    score += getScore('X')
                case 'B':
                    score += getScore('Y')
                case 'C':
                    score += getScore('Z')
        case 'Z':
            #Win
            score += 6
            match l[0]:
                case 'A':
                    score += getScore('Y')
                case 'B':
                    score += getScore('Z')
                case 'C':
                    score += getScore('X')

print('Part Two -', score)
