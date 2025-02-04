#!/usr/bin/env python3

def main():
    rows = []

    with open('testinput.txt', 'r') as file:
        for line in file:
            rows.append(line.strip())

    count = 0
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == 'A':
                count += checkXmas(i, j, rows)

    print('X-MAS count is {0}'.format(count))

def checkXmas(i, j, rows):
    if i < 1 or j < 1 or i > len(rows) - 2 or j > len(rows[0]) - 2:
        return 0
    return int(
        ((rows[i - 1][j - 1] == 'M' and rows[i + 1][j + 1] == 'S') or 
            (rows[i - 1][j - 1] == 'S' and rows[i + 1][j + 1] == 'M')) and 
        ((rows[i - 1][j + 1] == 'M' and rows[i + 1][j - 1] == 'S') or 
            (rows[i - 1][j + 1] == 'S' and rows[i + 1][j - 1] == 'M')))

main()