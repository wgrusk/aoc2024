# No duplicate pages in any print order
with open('input.txt', 'r') as file:
    for line in file:
        if not line or '|' in line:
            continue
        pages = line.split(',')
        seen = set()
        for page in pages:
            if page in seen:
                print('duplicate page')
            seen.add(page)