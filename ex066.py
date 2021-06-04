import random, time
res=""
contwin=0
print(f"""{"-="*15}
{"VAMOS JOGAR PAR OU ÍNPAR":^30}
{"-="*15}""")

while True:

    num = int(input("Diga um valor: "))
    comp_num = random.randint(1,10)
    parimp = input("Par ou Ímpar [P/I]: ").strip().upper()[0]
    print("-"*30)
    if (num + comp_num)%2 == 0 :
        res= "PAR"
    else:
        res = "IMPAR"

    print(f"Você jogou {num} e o computador jogou {comp_num} com o total de {num+comp_num} deu {res}")
    print("-" * 30)
    if parimp == res[0]:
        print(f"VOCÊ GANHOU!!\n{'-'*30}\nVamos jogar novamente...")
        contwin +=1
        time.sleep(2)
    else:
        print("VOCÊ PERDEU!")
        print("-="*15)
        print(f"GAME OVER você venceu {contwin} vezes")
        break