num = int(input( "Digite um número: "))
cont=0
lista =[]
for i in range(1,num+1):
    if num % i == 0:
        cont += 1
        lista.append(i)

       # print(f"\033[0;33m{i}\033[m",end=" ")
    #else:
       # print(f"\033[0;31m{i}\033[m",end=" ")
if cont == 2:
    print(f"\n\n{num} É um número primo!")
else:
    print(f"\n\n{num} NÃO É um número primo! É divisivel pelos números:\n\033[0;33m{lista}\033[m")


# \033[0;33;44m  ex: print("\033[1;31;42m Hello World \033[m")