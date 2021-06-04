"""
num = str(input("Informe um número, entre 0 e 9999: "))
uni = ["unidade","dezena","centena","milhar"]
print(f"Analisando o número {num}!")
for i in range(4):
      print(f"{uni[i]}: {num[len(num)-i-1]}")
"""

num = int(input("Informe um número, entre 0 e 9999: "))
uni = ["unidade","dezena","centena","milhar"]
res = 0
list=[]
divisor=1000
print(f"Analisando o número {num}!")
for i in range(4):
    res= num//divisor
    list.append(res)
    num-=divisor*list[i]
    divisor//=10
list.reverse()
for i in range(4):
    print(f"{uni[i]}: {list[i]}")