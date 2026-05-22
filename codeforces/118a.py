w = str(input())

change = []

for i in w:
    if i in 'aeiouyAEIOUY':
        continue
    else:
        change.append('.' + i.lower())


print(''.join(change))
