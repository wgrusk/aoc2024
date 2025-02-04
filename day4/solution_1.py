#!/usr/bin/env python3

def main():
    rows = []

    with open('input.txt', 'r') as file:
        for line in file:
            rows.append(line.strip())

    count = 0
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == 'X':
                # Each returns 1 if XMAS is found or 0 if not
                count += scanLeft(i, j, rows)
                count += scanRight(i, j, rows)
                count += scanUp(i, j, rows)
                count += scanDown(i, j, rows)
                count += scanUpLeft(i, j, rows)
                count += scanUpRight(i, j, rows)
                count += scanDownLeft(i, j, rows)
                count += scanDownRight(i, j, rows)

    print('XMAS count is {0}'.format(count))

def scanLeft(i, j, rows):
    if j < 3:
        return 0
    return int(rows[i][j - 1] == 'M' and rows[i][j - 2] == 'A' and rows[i][j - 3] == 'S')

def scanRight(i, j, rows):
    if j > len(rows[0]) - 4:
        return 0
    return int(rows[i][j + 1] == 'M' and rows[i][j + 2] == 'A' and rows[i][j + 3] == 'S')

def scanDown(i, j, rows):
    if i > len(rows) - 4:
        return 0
    return int(rows[i + 1][j] == 'M' and rows[i + 2][j] == 'A' and rows[i + 3][j] == 'S')

def scanUp(i, j, rows):
    if i < 3:
        return 0
    return int(rows[i - 1][j] == 'M' and rows[i - 2][j] == 'A' and rows[i - 3][j] == 'S')
    
def scanUpLeft(i, j, rows):
    if i < 3 or j < 3:
        return 0
    return int(rows[i - 1][j - 1] == 'M' and rows[i - 2][j - 2] == 'A' and rows[i - 3][j - 3] == 'S')
    
def scanDownRight(i, j, rows):
    if i > len(rows) - 4 or j > len(rows[0]) - 4:
        return 0 
    return int(rows[i + 1][j + 1] == 'M' and rows[i + 2][j + 2] == 'A' and rows[i + 3][j + 3] == 'S')

def scanDownLeft(i, j, rows):
    if j < 3 or i > len(rows) - 4:
        return 0
    return int(rows[i + 1][j - 1] == 'M' and rows[i + 2][j - 2] == 'A' and rows[i + 3][j - 3] == 'S')
    
def scanUpRight(i, j, rows):
    if i < 3 or j > len(rows[0]) - 4:
        return 0
    return int(rows[i - 1][j + 1] == 'M' and rows[i - 2][j + 2] == 'A' and rows[i - 3][j + 3] == 'S')

main()