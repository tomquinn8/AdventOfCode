#! /usr/bin/env python3

with open('Day1-input.txt', 'r') as f:
    lines = [_.rstrip() for _ in f]

number_words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
total = 0
for l in lines:
    for h in number_words:
        # Replace word with number but leave first and last letter in case it overlaps
        l = l.replace(h, h[0] + number_words[h] + h[-1])
    numbers = ''.join([c for c in l if c.isnumeric()])
    i = int(numbers[0] + numbers[-1])
    total += i

print(total)
