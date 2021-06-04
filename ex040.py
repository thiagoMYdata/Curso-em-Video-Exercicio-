import time
print("avalidor de triângulos")
l1,l2,l3 = float(input("Digite o valor do lado 1: ")),float(input("Digite o valor do lado 2: ")),float(input("Digite o valor do lado 3: "))

print("[...]")
time.sleep(2)

if abs(l1-l3)<l2<l1+l3:
    print("Os segmentos de retas PODEM formar um triângulo", end=" ")
    if l1 == l2 == l3:
        print("EQUILÁTERO!")
    elif l1 == l2 or l1 == l3 or l2 ==l3:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos de retas NÂO PODEM formar um triângulo")