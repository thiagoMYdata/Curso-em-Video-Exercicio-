from datetime import date

date, cont = date.today().year, 0
menor, maior = 0, 0

for i in range(1, 7 + 1):
    pes_nas = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    age = date - pes_nas
    if age >= 21:
        maior += 1
    else:
        menor += 1

if maior and menor >0:
    print(f"Ao todo tivemos {maior} maiores de idade\ne tambem tivemos {menor} menores.")
elif maior > 0 and menor == 0:
    print(f"Ao todo tivemos {maior} maiores de idade")
else:
    print(f"Ao todo tivemos {menor} menor de idade")
