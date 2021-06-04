city= str(input("Em qual cidade você nasceu?: ")).strip().lower()

if city.find("santo") == 0:
    print(True)
else:
    print(False)
