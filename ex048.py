sum = 0
for i in range(6):
    num = int ( input("Digite um número: "))
    if num % 2 == 0 :
        sum+=num
print(f"A soma dos números pares somente { sum } é igual.")
