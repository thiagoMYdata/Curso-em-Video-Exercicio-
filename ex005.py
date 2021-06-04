num , som= int(input("digite o número de notas: ")), 0
for cont in range(num):
    som += float(input("digite a nota:"))
print(f"sua média foi de {som/num}")