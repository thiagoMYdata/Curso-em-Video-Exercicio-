time =( "America MG" ,"Atletico PR", "Atletico GO", "Atletico MG", "Bahia", "Ceara", "Chapecoense", "Corinthians" ,"Cuiaba", "Flamengo", "Fluminense", "Fortaleza", "Gremio", "Internacional", "Juventude", "Palmeiras", "Bragantino", "Santos", "Sao Paulo" ,"Sport")
index= 0

print(f"A ordem dos times está: {time}\n{'=-'*50}")
print(f"Top 5: {time[:5]}\n{'=-'*50}")
print(f"Ultimos 4 times: {time[-5:]}\n{'=-'*50}")
print(f"Ordem alfabética dos times: {sorted(time)}\n{'=-'*50}")

while True:
    if time[index] == "Chapecoense":
        break
    index+=1
print(f" A Chapecoense está na posição: {index + 1}")