
num=cont=sum=0
while True:
    num =int(input("Digite um número (999 para parar): "))
    if num == 999:
        break
    cont+=1
    sum+=num
print(f"A soma dos {cont} é de {sum}")