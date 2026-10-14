n, h = map(int, input().split())

list_of_n = list(map(int,input().split()))

size=0

for w in list_of_n:
    if w > h:
        size += 2
    else:
        size += 1
        
        
print(size)