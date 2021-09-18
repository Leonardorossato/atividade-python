import math

cB = float(input("Digite um valor para o cateto oposto : "))
cA = float(input("Digite um valor para o cateto adjacente : "))

Triangulo = math.sqrt(cA**2 +cB**2)

print(f"O valor do triangulo é de : {Triangulo: .2f}")