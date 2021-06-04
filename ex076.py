list=[]
menor= maior = 0
memorise_maior= []
memorise_menor = []
for i in range(4):
    list.append(int(input("Digite um número: ")))
    if i == 0:
        maior = list[0]
        memorise_maior.append(i)

    elif maior < list[i]:
        maior = list[i]
        memorise_maior = []
        memorise_maior.append(i)
    elif maior == list[i]:
        maior = list[i]
        memorise_maior.append(i)

    if i == 0 :
        menor = list[0]
        memorise_menor.append(i)
    elif menor > list[i]:
        menor = list[i]
        memorise_menor= []
        memorise_menor.append(i)
    elif menor == list[i]:
        menor = list[i]
        memorise_menor.append(i)


print(f"-_"*30)
print(f"O maior digito digitado foi {maior} nas posições {memorise_maior}")
print(f"O menor digito digitado foi {menor} nas posições {memorise_menor}")