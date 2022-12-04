#!/usr/bin/env python3

with open('Day4-input.txt','r') as f:
    lines = [_.rstrip() for _ in f]

count1 = 0
count2 = 0

for l in lines:
    elf1 = [int(i) for i in l.split(',')[0].split('-')]
    elf2 = [int(i) for i in l.split(',')[1].split('-')]
    #Part One
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        count1 += 1
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        count1 += 1

    #Part Two
    if elf1[0] <= elf2[1] and elf1[0] >= elf2[0]:
        count2 += 1
    elif elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
        count2 += 1
    elif elf2[0] <= elf1[1] and elf2[0] >= elf1[0]:
        count2 += 1
    elif elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
        count2 += 1

print('Part One -', count1)
print('Part Two -', count2)
