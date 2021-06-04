print(F"{'='*6}LOJAS THIAGO{'='*6}")
pre = float(input("Preço das compras: R$"))*100

print("""
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] 2x no cartão: preço formal 
[4] 3x ou mais no cartão COM 20% de juros
""")

opc = int(input("Qual a opção: "))

if 0 < opc <5:
    if opc == 1 :
        print(f"Sua compra de {pre/100:.2f} vai custar no fim R${(pre*0.9)/100:.2f}")
    elif opc == 2:
        print(f"Sua compra de {pre/100:.2f} vai custar no fim R${(pre*0.95)/100:.2f}")
    elif opc == 3:
        print(f"Sua compra de {pre/100:.2f} vai custar no fim R${pre/100:.2f} com duas parcelas de R${pre/200:.2f} sem juros")
    else:
        nparc=int(input("Qual o número de parcelas?: "))
        print(f"Sua compra de {pre/100:.2f} vai custar no fim R${pre*1.20/100:.2f} com o valor das parcelas de R${pre*1.20/(100*nparc):.2f} com juros")
else:
    print("Opção invalida")