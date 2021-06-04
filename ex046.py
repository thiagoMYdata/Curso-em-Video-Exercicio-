cont = 0
som = 0
for i in range(1,499+1,2):
    if i % 3 == 0:
        cont+=1
        som+=i

print(f"A soma dos {cont} valores solicitados é {som} ")