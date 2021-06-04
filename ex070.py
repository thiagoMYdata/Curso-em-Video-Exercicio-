nomenclatura=("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","dose","treze","catoreze","quinze","dezeseis","dezesete","dezoito","dezenove","vinte")

num=int(input("Digite um número entre 0 e 20: "))
while 0 > num or num > 20 :
    num = int(input("Digite um número entre 0 e 20: "))
print(f"Você digitou o número {nomenclatura[num]}")


