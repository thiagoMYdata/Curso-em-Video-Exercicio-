vel= int(input("Qua a velocidade atual do seu carro?: "))

if vel <= 80:
    print(f"Tudo nós conformes, sua velocidade de {vel} não ultrapassou o limite de 80km/h ")
else:
    print(f"MUTADO!! Você EXECEDEU os 80km/h\nDeverá pagar uma multa de R${(vel-80) * 7:.2f} ")