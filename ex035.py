from random import randint
num= int(input("Digite um número: "))
list, name=[bin(num),oct(num),hex(num)],["binário","octal ","hexadecimal"]
elem= randint(0,2)
print(f"Seu número {num} está na base decimal em {name[elem]} fica {list[elem]}")
