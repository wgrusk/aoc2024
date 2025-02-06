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
    Determine if pages are in correct printable order. If so return 0, if not reorder the pages and
    return the middle page number of the properly ordered pages.
    """
    seen = set()
    allpages = set(pages)
    for page in pages:
        if page in order and (order[page] & allpages) > seen:
            # Some prerequisite pages are not present in order
            fixed = reorderPages(pages, order)
            return int(fixed[len(fixed) // 2])
        seen.add(page)
    return 0

def reorderPages(pages, order):
    newOrder = []

    def insertInOrder(page):
        pageReqs = set(newOrder) & order[page] if page in order else {}
        for i in range(len(newOrder)):
            if not pageReqs:
                newOrder.insert(i, page)
                return
            pageReqs.discard(newOrder[i])
        newOrder.append(page)

    for page in pages:
        insertInOrder(page)

    return newOrder

main()