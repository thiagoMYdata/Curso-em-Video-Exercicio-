n1,n2 = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print(f"Tirando {n1} e {n2}, a media do aluno é: {media:.2f}")
if media >= 7:
    print("APROVADO!!")
elif  5 > media < 7:
    print("RECUPERAÇÃO!")
else:
    print("REPROVADO!!!")