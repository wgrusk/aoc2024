#!/usr/bin/env python3

def isSafe(report):
    prev = int(report[0])
    direction = int(report[1]) - int(report[0])
    direction = direction / abs(direction) if direction != 0 else 0
    for n in report[1:]:
        n = int(n)
        diff = abs(n - prev)
        if diff < 1 or diff > 3:
            return False
        dir = (n - prev) / diff
        if dir != direction:
            return False
        prev = n
    return True

safe_reports = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = line.split()
        if isSafe(report):
            safe_reports += 1

print('the number of safe reports is %d' % safe_reports)
