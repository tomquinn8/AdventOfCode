#!/usr/bin/env python3

with open('Day5-input.txt','r') as f:
    lines = [_.rstrip('\n') for _ in f]

stacks = []
for _ in range(0,9):
    stacks.append([])

start = [(i, _) for i, _ in enumerate(lines) if _.startswith(' ')][0][0]

#Part One
for i in range(start - 1, -1, -1):
    for j in range(0,9):
        if lines[i][(j * 4) + 1] != ' ':
            stacks[j].append(lines[i][(j * 4) + 1])

for l in lines[start + 2:]:
    line = l.split(' ')
    qty = int(line[1])
    frm = int(line[3]) - 1
    to = int(line[5]) - 1
    for _ in range(qty):
        stacks[to].append(stacks[frm].pop())

print('Part One -', ''.join([s[-1] for s in stacks])) 

#Part Two
stacks = []
for _ in range(0,9):
    stacks.append([])

for i in range(start - 1, -1, -1):
    for j in range(0,9):
        if lines[i][(j * 4) + 1] != ' ':
            stacks[j].append(lines[i][(j * 4) + 1])

for l in lines[start + 2:]:
    line = l.split(' ')
    qty = int(line[1])
    frm = int(line[3]) - 1
    to = int(line[5]) - 1
    tmp = []
    for _ in range(qty):
        tmp.append(stacks[frm].pop())
    for i in reversed(tmp):
        stacks[to].append(i)

print('Part Two -', ''.join([s[-1] for s in stacks])) 
