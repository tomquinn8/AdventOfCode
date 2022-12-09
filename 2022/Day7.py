#!/usr/bin/env python3

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

with open('Day7-input.txt','r') as f:
    lines = [l.rstrip() for l in f] 

dirs = {'/': Dir('/', None)} 
current_dir = dirs['/'].name
previous_dir = None

for l in lines[2:]:
    if l.startswith('$'):
        #command
        pass
    else:
        if l.startswith('dir'):
            dirs[l.split(' ')[1]] = Dir(l.split(' ')[1], current_dir)
            dirs[current_dir].dirs.append(l.split(' ')[1]) 
        else:
           dirs[current_dir].files.append(int(l.split(' ')[0])) 
