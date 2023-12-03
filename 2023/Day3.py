#! /usr/bin/env python3

import re

lines = list(open('Day3-input.txt', 'r'))
p1_total = 0
symbols = {} 
gears = {}

for row in range(len(lines[0]) - 1):
    for col in range(len(lines)):
        if lines[row][col] not in '0123456789.':
            symbols[(row, col)] = lines[row][col]
            if lines[row][col] == '*':
                gears[(row,col)] = []

for row_num, row in enumerate(lines):
    for c in re.finditer(r'\d+', row):
        possibilities = []
        for i in range(c.start() - 1, c.end() + 1):
            possibilities.append((row_num - 1, i))
            possibilities.append((row_num, i))
            possibilities.append((row_num + 1, i))
        valid = False
        for p in possibilities:
            if p in symbols:
                valid = True
                if p in gears:
                    gears[p].append(int(c.group()))
        if valid:
            p1_total += int(c.group())
print('Part One -', p1_total)
p2_total = 0
for g in gears:
    if len(gears[g]) == 2:
        p2_total += (gears[g][0] * gears[g][1])
print('Part Two -', p2_total)
