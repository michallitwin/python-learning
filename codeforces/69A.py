n = int(input())

x_sum = []
y_sum = []
z_sum = []

for i in range(n):
    a = input()
    wspolrzedne = a.split()
    x_sum.append(int(wspolrzedne[0]))
    y_sum.append(int(wspolrzedne[1]))
    z_sum.append(int(wspolrzedne[2]))


if sum(x_sum) == 0 and sum(y_sum) == 0 and sum(z_sum) == 0:
    print('YES')
else:
    print('NO')


