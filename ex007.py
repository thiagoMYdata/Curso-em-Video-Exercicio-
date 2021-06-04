num , line = int(input("Digite um número para escolher a tabuada:")), "-"*15
print(line)
for cont in range(100+1):
    print(f"{num} X {0+cont} = {cont*num}")
print(line)