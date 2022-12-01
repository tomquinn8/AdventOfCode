#!/usr/bin/env python3

with open('Day1-input.txt','r') as f:
    lines = [_.rstrip() for _ in f]

elves = []
i = 0

for l in lines:
    if l:
        i += int(l)
    else:
        elves.append(i)
        i = 0

print('Top Elf -', max(elves))
print('Top Three Elves -', sum(sorted(elves)[-3:]))
