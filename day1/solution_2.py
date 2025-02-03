#!/usr/bin/env python3

first = []
second = {}

with open('input.txt', 'r') as file:
    for line in file:
        [f, s] = line.split()
        first.append(f)
        if s in second:
            second[s] += 1
        else:
            second[s] = 1

similarity = 0
for f in first:
    similarity += int(f) * second[f] if f in second else 0

print('total similarity is: %d' % similarity)