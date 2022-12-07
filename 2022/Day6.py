#!/usr/bin/env python3

with open('Day6-input.txt','r') as f:
    input_str = f.read()

for i in range(4,len(input_str)):
    if len(set(input_str[i - 4:i])) == 4:
        print('Part One -',i)
        break

for i in range(14,len(input_str)):
    if len(set(input_str[i - 14:i])) == 14:
        print('Part Two -',i)
        break
