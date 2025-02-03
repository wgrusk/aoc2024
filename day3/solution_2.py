#!/usr/bin/env python3

import re

MUL_PATTERN = 'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
DO_PATTERN = 'do\(\)'
DONT_PATTERN = 'don\'t\(\)'
INSTRUCTION_PATTERN = MUL_PATTERN + '|' + DO_PATTERN + '|' + DONT_PATTERN

contents = None
with open('input.txt', 'r') as file:
    contents = file.read()

total = 0
enabled = True
for match in re.finditer(INSTRUCTION_PATTERN, contents):
    if match.group(0) == 'do()':
        enabled = True
    elif match.group(0) == 'don\'t()':
        enabled = False
    elif enabled:
        total += int(match[1]) * int(match[2])

print('total is {0}'.format(total))