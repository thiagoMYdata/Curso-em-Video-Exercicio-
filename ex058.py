nfatorial=int(input("Qual fatorial você quer: "))
resulfatorial=1
cont=0
while cont != nfatorial:
    resulfatorial *= (nfatorial-cont)
    cont+=1
print(f"O Resultado é {resulfatorial}")
