from random import randint

print("Olá sou seu computador\ne acabei de pensar em um número de 1 a 10 \nserá que você consegue adivinhar qual foi?")
comp_num = randint(1, 10)
chute = 0
cont = 0
while chute != comp_num:
    chute = int(input("Qual é seu palpite?: "))
    cont += 1
    if chute < comp_num:
        print("mais...tente novamente")
    else:
        print("menos...tente novamente")
print(f"Você ACERTOU em {cont} tentativas")
