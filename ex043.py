import random, time

print("""Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

jogadas = ["PEDRA","PAPEL","TESOURA"]

mao_1 , pc = int(input("Qual é a sua jogada?: ")), random.randint(0,2)

if 0 <= mao_1 <= 2:
    for i in range(3):
        list = ["JO","KEN","PO!!!"]
        print(list[i])
        time.sleep(1)

    print(f"{'-+=+' * 10}\n"
          f"COMPUTADOR jogou {jogadas[pc]}\n"
          f"JOGADOR jogou {jogadas[mao_1]}\n"
          f"{'-+=+' * 10}")
    if mao_1 == pc:
        print("COMPUTADOR e JOGADOR EMPATAM")
    elif mao_1 == 0 and pc == 2 or mao_1 == 1 and pc == 0 or mao_1 == 2 and pc == 1:
        print("JOGADOR VENCEU")
    else:
        print("COMPUTADOR VENCEU")
else:
    print("MOVIMETO ILEGAL")
