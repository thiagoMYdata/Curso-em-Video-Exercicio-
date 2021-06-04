rept= "S"
cont = num = sum = menor = maior = 0
while rept == "S":
    num = int(input("Digite um número: "))
    if cont == 0:
        maior = num
        menor = num
    cont += 1
    sum += num
    if maior < num:     maior = num
    elif menor > num:   menor = num
    rept = input("Quer continuar [S/N]:").strip().upper()
print(f"Você digitou {cont} números e a média foi m {sum / cont}\nO maior valor foi {maior} e o menor foi {menor}")
