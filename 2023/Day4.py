#! /usr/bin/env python3

import re

lines = list(open('Day4-input.txt', 'r'))

p1_total = 0
for line in lines:
    line = line.rstrip()
    winning_numbers = [i for i in line[7::].split('|')[0].split(' ') if len(i)>0]
    my_numbers = [i for i in line.split('|')[1].split(' ') if len(i)>0]
    winners = set(winning_numbers).intersection(my_numbers)
    points = 0
    if len(winners)>0:
        points = 1
        for i in range(len(winners) - 1):
            points = points * 2
    p1_total += points

print("Part One -", p1_total)
