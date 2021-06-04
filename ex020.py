name= input("Digite seu nome:").strip()
namelist= name.split()
namespace= "".join(namelist)
print(f"Seu nome em maiúsculas é {name.upper()}"),print(f"Seu nome em minúsculas é {name.lower()}"),print(f"Seu nome tem ao todo {len(namespace)} letras"), print(f"Seu primeiro nome é {namelist[0]} e ele tem {len(namelist[0])} letras")