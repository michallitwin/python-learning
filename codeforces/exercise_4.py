string = input().lower()
words = []

for i in string:
    if i in words:
        continue
    else:
        words.append(i)

if len(words) % 2 == 0:
    print("CHAT WITH HER!")

else:    
    print("IGNORE HIM!")
