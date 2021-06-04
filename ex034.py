# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa, sal, nyears = float(input("Digite o valor da casa: ")), float(input("Digite seu salário:")), int(input("Digite o número de anos que quer pagar o valor total da casa, sem juros: "))
pres=casa/(nyears*12)


if pres <= sal*0.30:
    print(f"Para pagar uma casa de R${casa:.2f} em {nyears} anos, a prestação sera de R${pres:.2f} ")
    print("Seu empréstimo bancário foi APROVADO!")
else:
    print(f"Para pagar uma casa de R${casa:.2f} em {nyears} anos, a prestação sera de R${pres:.2f} ")
    print("Seu empréstimo bancário foi NEGADO!")





