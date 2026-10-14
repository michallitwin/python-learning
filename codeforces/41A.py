a = str(input())
b = str(input())

word = []

for w in reversed(a):
    word.append(w)

final_word = "".join(word)    

if final_word == b:
    print('YES')
else:
    print("NO")