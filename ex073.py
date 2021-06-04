tupla = (int(input("Digite um número: ")),int(input("Digite outro número: ")),int(input("Digite mais um número: ")),int(input("Digite um ultimo número: ")))
index = cont_9 = passo = cont_3 = 0
memorise = -1
concatenar=""
while True:
    if passo == len(tupla) :
        break
    if tupla[index] == 9:
        cont_9+=1
    elif tupla[index] == 3 and cont_3 == 0:
        memorise = index + 1
        cont_3+=1
    elif tupla[index] % 2 == 0:
        concatenar += f"{tupla[index]} "
    passo+=1
    index+=1

if cont_9 == 0:
    print("Não foi encontrado nenhum 9")
else:
    print(f"O número total de noves encontrados foi {cont_9}")



if memorise == -1:
    print("Não foi encontrado nenhum 3")
else:
    print(f"O número 3 foi encontrado na posição {memorise}")



if len(concatenar) == 0:
    print("Não foi encontrado nenhum número par")
else:
    print(f"O(s) número(s) par(es) encontrado(s): {concatenar}")
