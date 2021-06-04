n1, n2, n3 = int(input("digite o primeiro número:")), int(input("digite o segundo número:")), int(
    input("digite o terçeiro número:"))
menor = n1
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f"O maior número é {maior} e o menor é {menor}")

"""
if n1 > n2 and n1> n3:
    if n2>n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif n2>n1 and n2> n3:
        if  n1> n3:
            print(n2,n1,n3)
        else:
            print(n2, n3, n1)
elif n3>n1 and n3>n2:
    if n1> n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)
"""
################################################################
