n = int(input("Quantos números da sequência: "))
x,y=0,1
cont=0

if n == 1:
    print("0",end=" → ")
elif n ==2:
    print("0 → 1",end=" → " )
elif n>2:
    n-=2
    print("0 → 1 → ",end="")
    while cont != n:
        sum = x + y
        print(sum,end=" → ")
        x = y
        y=sum
        cont+=1





print("fim")