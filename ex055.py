gender="vazio"
findMorF = 0

while findMorF != 1:
    gender = input("digite seu género é [F/M]").upper()
    if gender == "F":
        findMorF+=1
        gender = "feminino"
    elif gender == "M":
        findMorF+=1
        gender = "Masculino"
    else:
        print("Valor de género inválido")
print(f"Seu género é {gender}")
