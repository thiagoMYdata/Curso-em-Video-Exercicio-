import math
co , ca = float(input("Comprimento do cateto oposto: ")), float(input("Comprimento do cateto adjacente: "))
#h=math.sqrt(math.pow(co,2)+ math.pow(ca,2))


h=math.hypot(ca,co)

print(f"A hipotenusa vai medir {h:.2f}")