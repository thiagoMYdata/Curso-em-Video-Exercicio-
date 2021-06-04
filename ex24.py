phr= str( input("Digite alguma frase: ")).strip().lower()

print(f"""A letra "A" apareceu {phr.count("a")} vezes\nA primeira letra "A" apareceu na posição {phr.find("a")+1}\nA ultima letra "A" apareceu na posição {phr.rfind("a")+1} """)