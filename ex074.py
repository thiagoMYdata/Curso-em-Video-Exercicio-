lista_preco = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Trasnferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32 , "Canetas", 22.30, "Livro", 34.90)

index = 0

print(f"{'-'*50}\n{'LISTAGEM DE PREÇOS':^50}\n{'-'*50}")

while True:
    if index == len(lista_preco):
        break
    print(f" {lista_preco[index]:.<38}R${lista_preco[index+1]:>8.2f} ")
    index+=2

print("-"*50)