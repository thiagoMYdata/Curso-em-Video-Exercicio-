import random
list,dias=[],["Segunda","Terça","Quarta","Quinta","Sexta"]
for i in range(4):
    list.append(input("student's name:"))
for i in range(5):
    random.shuffle(list)
    print(f"A ordem sorteada na {dias[0+i]} será {list} ")

"""
import random
test_list = [1, 4, 5, 6, 3]
print ("The original list is : " + str(test_list))
random.shuffle(test_list)
print ("The shuffled list is : " +  str(test_list))
"""