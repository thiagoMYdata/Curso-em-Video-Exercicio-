continuar = "S"
menor = presun = cont_pre = volta = preco_guard = 0
produto_name_guard = ""

print(f"{'-' * 45}\n{'SUPERMERCADO SUPER BARATÃO':^45}\n{'-' * 45}")
while True:
    if continuar == "N":
        break
    while continuar == "S":
        produto_name = input("Digite o nome do produto: ").strip().capitalize()
        preco = float(input("Preço R$:"))
        presun += preco
        if preco > 1000:
            cont_pre += 1
        elif volta == 0:
            menor = preco
            produto_name_guard = produto_name
            preco_guard = preco
            volta+=1
        elif menor > preco:
            menor = preco
            produto_name_guard = produto_name
            preco_guard = preco
        continuar = input("Quer continuar [S/N]: ").strip().upper()
        while continuar not in "SN":
            continuar = input("Quer continuar [S/N]: ").strip().upper()

print(f"{' fim do programa ':=^45}")

print(f"O valor total de toda a compra foi de R${presun:.2f}\n"
      f"Dentre a sua compra o número de produtos que excedem R$1000 são {cont_pre}\n"
      f"O produto mais barato foi {produto_name_guard} que custou a bargatela de R${preco_guard} ")
