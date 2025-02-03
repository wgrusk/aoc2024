#!/usr/bin/env python3

import re

MUL_PATTERN = 'mul\(([0-9]{1,3}),([0-9]{1,3})\)'

contents = None
with open('input.txt', 'r') as file:
    contents = file.read()

total = 0
for match in re.findall(MUL_PATTERN, contents):
    total += int(match[0]) * int(match[1])

print('total is {0}'.format(total))