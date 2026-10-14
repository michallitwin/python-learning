#k - the cost of the first banana
#n - the amount of money that the soldier has
#w - the amount of bananas that the soldier wants to buy

k, n, w = map(int, input().split())

cost = 0

for i in range(w):
    cost += k * (i + 1)
if cost > n:
    print(cost - n)
else:
    print(0)