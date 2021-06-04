num_list = []
while True:
    num_list.append(int(input("Digite um número: ")))
    continuar = input("Quer continuar [S/N]").strip().upper()[0]
    while continuar not in "SN":
        continuar = input("[VALOR INVÁLIDO] Quer continuar [S/N]").strip().upper()[0]
    if continuar == "N":
        break
print(f"Você digitou {len(num_list)} elementos")
print(f"Os valores em ordem decrescente são {list(reversed(sorted(num_list)))}")
if 5 in num_list:
    print("O valor 5 faz parte de sua lista!")
else:
    print("O valor 5 não faz parte da sua lista!")
