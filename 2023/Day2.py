#! /usr/bin/env python3

with open('Day2-input.txt', 'r') as f:
    lines = [_.rstrip() for _ in f]

rules = {'red': 12, 'green': 13, 'blue': 14}

p1_total = 0
p2_total = 0

for line in lines:
    game = int(line.split(':')[0].split(' ')[1])
    valid = True
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    for set_of_cubes in line.split(':')[1].split(';'):
        for cubes in set_of_cubes.split(','):
            cubes = cubes.lstrip().rstrip()
            qty = int(cubes.split(' ')[0])
            colour = cubes.split(' ')[1]
            if qty > rules[colour]:
                valid = False
            if qty > minimums[colour]:
                minimums[colour] = qty
    if valid != False:
        p1_total += game
    p2_total += minimums['red'] * minimums['green'] * minimums['blue']

print('Part One - ', p1_total)
print('Part Two - ', p2_total)



