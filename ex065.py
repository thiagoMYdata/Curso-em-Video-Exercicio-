tabu=cont=0

while True:
    print("-"*35)
    tabu=int(input("Quer ver a tabuada de qual valor?: "))
    if tabu < 0 :
        break
    cont=0
    while cont != 10:
        print(f"{tabu} X {cont+1} = {tabu*(cont+1)}")
        cont+=1