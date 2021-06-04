print(f"{' BANCO THIAGO ':=^35}\n{'=' * 35}")
valor = int(input("QUAL é o valor que quer sacar?: R$"))
nota = 50

while True:
    cont_cedulas = valor // nota
    print(f"total de {cont_cedulas} cédulas de R${nota}")
    valor -= nota * cont_cedulas
    if nota == 1:
        break
    elif nota == 50:
        nota = 20
    elif nota == 20:
        nota = 10
    elif nota == 10:
        nota = 5
    elif nota == 5:
        nota = 2
    elif nota == 2:
        nota = 1

print('=' * 35, "\nVolte sempre ao BANCO THIAGO,\ntenha um bom dia.")


"""
    if passo == 0:
        nota = 20
        passo += 1
    elif passo == 1:
        nota = 10
        passo += 1
    elif passo == 2:
        nota = 5
        passo += 1
    elif passo == 3:
        nota = 2
        passo += 1
    elif passo == 4:
        nota = 1
        passo += 1
"""

"""cont_cedulas= valor //50
print(f"total de {cont_cedulas} cédulas de R$50")
valor = valor-50*cont_cedulas

cont_cedulas= valor // 20
print(f"total de {cont_cedulas} cédulas de R$20")
valor = valor-20*cont_cedulas

cont_cedulas= valor //10
print(f"total de {cont_cedulas} cédulas de R$10")
valor = valor-10*cont_cedulas

cont_cedulas= valor //5
print(f"total de {cont_cedulas} cédulas de R$5")
valor = valor-5*cont_cedulas

cont_cedulas= valor //2
print(f"total de {cont_cedulas} cédulas de R$2")
valor = valor-2*cont_cedulas

cont_cedulas= valor //1
print(f"total de {cont_cedulas} cédulas de R$1")
valor = valor-1*cont_cedulas
"""
