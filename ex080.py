num_list, num_listpar, num_listinpar = [],[],[]
while True:
    num = int(input("Digite um número: "))
    num_list.append(num)
    if num % 2 == 0:
        num_listpar.append(num)
    else:
        num_listinpar.append(num)
    continuar = input("Quer continuar [S/N]: ").strip().upper()[0]
    while continuar not in "SN":
        continuar = input("[VALOR INVÁLIDO]Quer continuar [S/N]: ").strip().upper()[0]
    if continuar == "N":
        break
print(f"A lista completa é {num_list}"), print(f"A lista de pares é {num_listpar}"), print(f"A lista de inpares é {num_listinpar}")



"""continuar = "S"
while continuar != "N":
    num_list.append(int(input("Digite um número: ")))
    continuar = input("Quer continuar [S/N]: ")
    while continuar not in "SN":
        continuar = input("[VALOR INVÁLIDO]Quer continuar [S/N]: ")"""