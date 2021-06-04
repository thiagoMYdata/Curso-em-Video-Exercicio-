from math import sin,cos,tan,radians
ang =float(input("Digite um ângulo que você deseja: "))
rad = radians(ang)
print(f"O ângulo de {ang} tem o seno de {sin(rad):.2f}\nO ângulo de {ang} tem o cosseno de {cos(rad):.2f}\nO ângulo de {ang} tem a tangente de {tan(rad):.2f}")