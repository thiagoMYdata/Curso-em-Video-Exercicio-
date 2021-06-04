dis=int(input("Qual é a distância da sua viajem?: "))

print(f"Você está prestes a começar uma viagem de {dis}km")
if dis> 200:
    print(f"E o preço de sua passagem será de {dis*0.45}")
else:
    print(f"E o preço de sua passagem será de {dis*0.50}")
