sal= int(input("Qual o salário do seu funcionário? "))

if sal > 1250:
    print(f"Quem ganhava {sal} passa a ganhar R${sal*1.10:.2f} agora ")
else:
    print(f"Quem ganhava {sal} passa a ganhar R${sal * 1.15:.2f} agora")