height , weight = float(input("Qual a sua altura?: ")), float(input("Qual é seu peso?: "))
imc = weight / height**2

print( f"Seu Índice de Massa Corporal (IMC) é {imc:.2f} que classifica-o como", end=" ")
if imc < 18.5 :
    print("Abaixo do Peso")
elif 18.5 <imc < 25:
    print("Peso Ideal")
elif 25 < imc < 30:
    print("Sobrepeso")
elif 30 < imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")
