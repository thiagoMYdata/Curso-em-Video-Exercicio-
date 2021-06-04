num_list = []
continuar = "S"
while True:
    if continuar in "N":
        break
    num = int(input("Digite um número: "))
    if len(num_list) == 0:
        num_list.append(num)
        print(f"Valor {num} foi adicionado na posição 1")
    elif num in num_list:
        print(f"Valor não adicionado já existe um {num}")
    elif num > max(num_list):
        num_list.append(num)
        print(f"Valor {num} foi adicionado, no fim da lista ")
    else:
        for i in range(len(num_list)):
            if num < num_list[i]:
                num_list.insert(i,num)
                print(f"Valor {num} foi adicionado na posição {i+1} ")
                break
    continuar=input("Quer continuar [S/N]: ").strip().upper()[0]
    while continuar not in "SN":
        continuar=input("[VALOR INVÁLIDO] Quer continuar [S/N]: ").strip().upper()[0]

print(f"Os valores adicionados foram: {num_list}")

"""
======================================================================================================================

Como o sorted() funciona na lista: A função organiza todos os elementos em ordem

o que quero é a funcinalidade do sorted(), contudo quando um elemento for igual a outro quero que não seja adicionado

 if num < num_list[i]:
    num_list.insert(num,i)
"""