list_num = [int(input("Digite um número: "))]
print("valor ADICIONADO com sucesso...")
while True:
    continuar = input("Quer continuar [S/N]: ").strip().upper()[0]
    while continuar not in "SN":
        continuar = input("[VALOR INVÁLIDO] Quer continuar [S/N]: ").strip().upper()[0]
    if continuar == "N":
        break
    num = int(input("Digite um número: "))
    if num not in list_num:
        list_num.append(num), print("valor ADICIONADO com sucesso...")
    else:
        print("valor DUPLICADO não será adicionado")
print("-="*15)
print(sorted(list_num))