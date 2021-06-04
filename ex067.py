continuar = "S"
cont_age = cont_men = cont_women_under_age=0
while True:
    if continuar == "N":
        break

    while continuar == "S":
        print("CADASTRE UMA PESSOA")
        print("-" * 30)
        age = int(input("Idade: "))

        if age > 18 :
            cont_age+=1

        gender = input("Sexo [F/M]: ").strip().upper()[0]
        while gender not in "FM":
            gender = input("Sexo [F/M]: ").strip().upper()[0]
        if gender == "M":
            cont_men+=1
        elif gender == "F" and age < 18:
            cont_women_under_age+=1
        print("-" * 30)
        continuar = str(input("Quer continuar (S/N): ")).strip().upper()[0]
        while continuar not in "SN":
            continuar = str(input("Quer continuar (S/N): ")).strip().upper()[0]
        print("-" * 30)

print(f"O total de pessoas com mais de 18 anos: {cont_age}")
print(f"Ao todo temos {cont_men} homens cadastrados")
print(f"E temos {cont_women_under_age} mulheres com menos de 18 anos de idade")
