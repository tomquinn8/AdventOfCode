#!/usr/bin/env python3

with open('Day3-input.txt','r') as f:
    lines = [_.rstrip() for _ in f]

total = 0

for l in lines:
    letter = [c for c in l[:int(len(l)/2)] if c in l[int(len(l)/2):]][0]
    if letter.islower():
        total += ord(letter) - 96
    else:
        total += ord(letter) -38 

print('Part One -', total)

total = 0
for i in range(0,len(lines)-2,3):
    letter = [c for c in lines[i] if c in lines[i + 1] and c in lines[i + 2]][0]
    if letter.islower():
        total += ord(letter) - 96
    else:
        total += ord(letter) -38 

print('Part Two -', total)
