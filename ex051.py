frase = str(input("Digite uma frase: ")).strip().lower()
reverse = frase[::-1]

print(f"frase: {frase} |=| frase invertida: {reverse}")
if "".join(frase.split()) == "".join(reverse.split()):
    print("É um palíndromo")
else:
    print("NÃO É um palíndromo")
