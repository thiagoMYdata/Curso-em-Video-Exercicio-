import datetime

year= int(input("Digite o ano para saber se foi bissexto: "))

if year == 0:
    year=datetime.date.today().year


if year% 4 ==0 and year % 100 != 0 or year% 400 == 0:
    print(f"{year}  é bissexto!")
else:
    print(f"{year} NÃO é bissexto!")
