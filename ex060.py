a1,r = int(input("Qual é o primeiro termo: ")),int(input("Qual é a razão da pa: "))
cont= 0
validador = 1
n, nmax = 1, 10
while validador != 0 :
    while cont != nmax:
        an = a1 + (n - 1) * r
        cont+=1
        n+=1
        print(an, end=" → ")
    cont=0
    print("fim")
    validador =int(input("Quantos termos a mais você quer mostrar: "))
    nmax = validador

print("PROGRAMA ENCERRADO")
