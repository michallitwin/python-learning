n = input()

licznik = 0

# Przechodzimy przez cały tekst i tylko zliczamy 4 i 7
for i in range(len(n)):
    if n[i] == "4" or n[i] == "7":
        licznik += 1

if licznik == 4 or licznik == 7:
    print("YES")
else:
    print("NO")