import random
name1,name2,name3,name4 = input("Primeiro aluno: "),input("Segundo aluno: "),input("Terceiro aluno: "), input("Quarto aluno: ")
list=[name1,name2,name3,name4]
print(random.choice(list))
