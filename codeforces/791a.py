limak, bob = map(int, input().split())

lata = 0 

while limak <= bob:
    limak = limak * 3
    bob = bob * 2 
    lata += 1

print(lata)

#The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight
#  of Limak and the weight of Bob respectively.

