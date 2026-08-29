n = int(input())

curr_n_of_people = 0
max_n_of_people = 0

for i in range(n):
    a, b = map(int, input().split())
    curr_n_of_people = curr_n_of_people - a + b
    if curr_n_of_people > max_n_of_people:
        max_n_of_people = curr_n_of_people
    return max_n_of_people