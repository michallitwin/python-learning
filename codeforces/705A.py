n = int(input())

fragmenty = []

for i in range(1, n + 1):
    if i % 2 != 0:
        fragmenty.append("I hate")
    else:
        fragmenty.append("I love")

# Łączymy fragmenty słowem "that" i na samym końcu dodajemy "it"
wynik = " that ".join(fragmenty) + " it"

print(wynik)
