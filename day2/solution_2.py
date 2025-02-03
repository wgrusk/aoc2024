#!/usr/bin/env python3

from itertools import *

shouldprint = False

def myprint(s):
    if shouldprint:
        print(s)

def isSafe(report, retry=True):
    myprint('isSafe(%s, %d)' % (report, retry))
    prev = int(report[0])
    direction = int(report[1]) - int(report[0])
    direction = direction / abs(direction) if direction != 0 else 0
    for i in range(1, len(report)):
        n = int(report[i])
        diff = abs(n - prev)
        myprint('comparing %d to %d, diff is %d' % (prev, n, diff))
        if diff < 1 or diff > 3:
            myprint('Fault at index %d' % i)
            if retry:
                myprint('retry')
                return isSafe(report[1:], False) or isSafe(report[:i] + report[i+1:], False) or isSafe(report[:i - 1] + report[i:], False)
            else:
                myprint('final failure')
                return False
        dir = (n - prev) / diff
        if dir != direction:
            myprint('Fault at index %d' % i)
            if retry:
                myprint('retry')
                return isSafe(report[1:], False) or isSafe(report[:i] + report[i+1:], False) or isSafe(report[:i - 1] + report[i:], False)
            else:
                myprint('final failure')
                return False
        prev = n
    myprint('success')
    return True

# TODO: complete non-brute force implementation
# def isSafe(report):
#     VALID_RANGE = range(1,4) # Range [1,3] inclusive
#     diffs = []
#     for i in range(len(report) - 1):
#         diffs.append(report[i] - report[i + 1])

#     in_range = filterfalse(lambda diff: abs(diff) < 4 and abs(diff) > 0, diffs) == []
    
    
    

safe_reports = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = line.split()
        if isSafe(report):
            safe_reports += 1

print('the number of safe reports is %d' % safe_reports)


# with open('testinput.txt', 'r') as file:
#     for line in file:
#         report = line.split()
#         result = isSafe(report)
#         expected = file.readline().strip() == 'True'
#         if result != expected:
#             print('Expected test case %s to have result %s but was %s' % (report, expected, result))
#             print('Debug output:')
#             shouldprint = True
#             isSafe(report)
#             shouldprint = False
