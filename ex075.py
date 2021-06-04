palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "fulturo")
palavra = ""
index =0
letra = 0
concatenar = ""
while True:
    if index == len(palavras):
        break
    palavra = palavras[index]

    while letra != len(palavra):
        if palavra[letra] == "a":
            concatenar+= "A "
        elif palavra[letra] == "e":
            concatenar += "E "
        elif palavra[letra] == "i":
            concatenar += "I "
        elif palavra[letra] == "o":
            concatenar += "O "
        elif palavra[letra] == "u":
            concatenar += "U "
        letra+=1
    print(f"Na palavra {palavra} temos {concatenar}")
    concatenar =""
    letra =0
    index+=1
