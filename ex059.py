print("Gerador de pa")
a1, r = int(input("digite o primeiro termo: ")), int(input("Digite a razão da pa: "))
cont = 0
n,nmax =1,10
while cont != nmax:
    an = a1 + ((n+cont)-1)*r
    print(an, end=" → ")
    cont+=1

print("FIM ")