n = int(input())
s = str(input())

D = []
A = []

for l in s:
    if l == "D":
        D.append(l)
    else:
        A.append(l)


if len(D) > len(A):
    print('Danik')

elif len(A) > len(D):
    print('Anton')
else: 
    print('Friendship')
    