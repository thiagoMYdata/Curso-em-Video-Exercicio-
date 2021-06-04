name= str(input("Digite seu nome: ")).strip().lower().split()
print(f"Seu primeiro nome é {name[0]}\nSeu ultimo nome é {name[len(name)-1]}")