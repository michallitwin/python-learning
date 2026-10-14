n = int(input())

opinins = list(map(int, input().split()))

if 1 in opinins:
    print("HARD")
else:
    print('EASY')