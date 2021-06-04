import datetime
user_date=int(input("Digite o ano de seu nascimento: "))
niver = str(input("já fez aniversário esse ano (s para sim e n não): ")).strip().lower()
date = datetime.date.today().year
fezniver = 0

if niver == "n":
    fezniver = 1

age= date- user_date - fezniver

print(F"O atleta tem {age} anos!")

if age <= 9:
    print("Clasificação: MIRIM")
elif 9 < age <= 14:
    print("Clasificação: INFANTIL")
elif 14< age <= 19:
    print("Clasificação: JÚNIOR")
elif 19< age <= 25:
    print("Clasificação: SÊNIOR")
else:
    print("Clasificação: MASTER")

