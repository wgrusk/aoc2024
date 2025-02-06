#!/usr/bin/env python3

def main():
    order = dict()
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            elif '|' in line:
                [first, second] = line.split('|')
                if not second in order:
                    order[second] = set()
                order[second].add(first)
            else:
                total += tabulateOrdering(line.split(','), order)

    print('Total of middle page numbers is {0}'.format(total))

def tabulateOrdering(pages, order):
    """
    Determine if pages are in correct printable order. If so return the middle page number, if not
    return 0.
    """
    seen = set()
    allpages = set(pages)
    for page in pages:
        if page in order and (order[page] & allpages) > seen:
            # Some prerequisite pages are not present in order
            return 0
        seen.add(page)
    return int(pages[len(pages)//2])

main()