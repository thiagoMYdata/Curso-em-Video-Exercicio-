print(f"""{"="*25}
{"10 termos de uma PA":^25}
{"="*25}""")
a1, r = int(input("Qual o primeiro termo?: ")),int(input( "Qual a razão da PA?: "))
n = 0
for i in range(1,10+1) :
    an = a1 + ((n+i) - 1) * r
    print(an, "→" ,end=" ")
print("Acabou")