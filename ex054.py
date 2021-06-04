cont_age, cont_woman, older_age = 0, 0, 0
name_memorise = "vazio"

for i in range(1, 4 + 1):
    print(f"{f' {i}ª pessoa ':-^21}")
    name = str(input("Nome: ")).strip().capitalize()
    age = int(input("idade: "))
    gender = str(input("Sexo [M/F]:")).strip().upper()
    cont_age += age
    if gender == "M":
        if i == 1:
            older_age = age
            name_memorise = name
        elif older_age < age:
            older_age = age
            name_memorise = name
    if gender == "F" and age < 20:
        cont_woman += 1

average = cont_age / 4

print(f"{' resulatado ':=^55}\n\n"
      f"A média da idade do grupo é: {average} anos\n"
      f"O homem mais velho tem {older_age} anos e se chama {name_memorise}\n"
      f"Ao todo são {cont_woman} mulher com menos de 20 anos")
