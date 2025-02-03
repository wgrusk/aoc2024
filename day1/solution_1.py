#!/usr/bin/env python3

first = []
second = []

with open('input.txt', 'r') as file:
    for line in file:
        [f, s] = line.split()
        first.append(int(f))
        second.append(int(s))


first.sort()
second.sort()

diff = 0
for i in range(len(first)):
    diff += abs(first[i] - second[i])

print('total difference is: %d' % diff)