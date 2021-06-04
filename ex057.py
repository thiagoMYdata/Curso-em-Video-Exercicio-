from time import sleep
n1,  n2 = int(input("Primeiro número: ")), int(input("Segundo número: "))
choice=0
efeito="="*35

while choice != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
""")
    choice = int(input("Qual sua opção: "))

    if choice == 1:
        print(f"A soma dos dois termos é {n1+n2}\n{efeito}")
        sleep(2)
    elif choice == 2 :
        print(f"A multiplicação dos dois termos é {n1*n2}\n{efeito}")
        sleep(2)
    elif choice == 3:
        if n1 == n2:
            print(f"Ambos os termos são iguais\n{efeito}")
            sleep(2)
        elif n1>n2:
            print(f"O termo {n1} é o maior entre os dois\n{efeito}")
            sleep(2)
        else:
            print(f"O termo {n2} é o maior entre os dois\n{efeito}")
            sleep(2)
    elif choice == 4:
        n1, n2 = int(input("Primeiro número: ")), int(input("Segundo número: \n{efeito}"))
        sleep(2)
    elif choice == 5:
        print(f"Programa finalizado")
    else:
        print(f"número inválido\n{efeito}")
        sleep(2)

