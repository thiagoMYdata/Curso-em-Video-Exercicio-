import datetime
yearuser = int(input("Digite o ano em que nasceu: "))
niver = str(input("já fez aniversário esse ano (s para sim e n não): ")).strip().lower()
yearpc = datetime.date.today().year
fezniver=0

if niver == "s":
    fezniver = 0
else:
    fezniver= 1

age = yearpc - yearuser - fezniver

if age == 18:
    print("Com 18 anos é o ano EXTADO do alistamento!! chegou a sua vez!")
elif age < 18:
    print(f"com {age} anos fantam {18-age} para o alistamento militar! Ainda não chegou a sua vez")
else:
    print(f"Com {age} já se passaram {abs(18-age)} anos da idade de se alistar! Já compriu com seu papel " )