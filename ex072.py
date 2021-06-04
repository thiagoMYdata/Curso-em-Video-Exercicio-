import random
random_num = (random.randint(0,10),     random.randint(0,10),    random.randint(0,10),       random.randint(0,10),       random.randint(0,10))
menor = maior = index = 0
while True:
    if index == len(random_num)-1:
        break
    if index == 0:
        menor = random_num[index]
        maior = random_num[index]
    index+=1
    if menor > random_num[index]:
        menor = random_num[index]

    elif maior < random_num[index]:
        maior = random_num [index]

print(F"OS NÚMEROS SÃO:\n{random_num}")
print(f"O maior número é {maior}\n"
      f"O menor número é {menor}")