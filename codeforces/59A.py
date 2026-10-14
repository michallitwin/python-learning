w = input()

lower = []
upper = []

for i in w:
    if i == i.lower():
        lower.append(i)
    else:
        upper.append(i)

if len(lower) >= len(upper):
    w = w.lower()
else:
    w = w.upper()

print(w)