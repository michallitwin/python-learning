n = int(input())
w = input()

to_delete = 0

for i in range(1,n):
    if w[i] == w[i-1]:
        to_delete += 1

print(to_delete)