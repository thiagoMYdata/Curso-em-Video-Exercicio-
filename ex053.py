string = []

for i in range(1, 5 + 1):
    kg = float(input(f"O peso da {i}ª pessoa: "))
    string.append(kg)

print(f"O maior número lido foi {max(string, key=float):.2f}kg\nO menor número lido foi {min(string, key=float):.2f}kg")
