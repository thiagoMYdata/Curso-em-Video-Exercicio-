"""
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
"""

efeito="-=-"*8

print(f"{efeito}\nAnalisador de triângulos\n{efeito}")
a,b,c= float(input("Primeiro lado: ")),float(input("segundo lado: ")),float(input("terçeiro lado: "))


if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
    print("O segmento acima PODE FORMAR um triângulo")
else:
    print("O segmento acima NÂO PODE FORMAR um triângulo")

