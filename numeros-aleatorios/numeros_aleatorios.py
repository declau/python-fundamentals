import random

numero = random.randint(0, 10)
# vai escolher aleatoriamente um numero entre 0 e 10
print(numero)
print("----------------------------")


# for em um range de números e depois ramdomizando o resultado
for numero in range(0, 10):
    numero = random.randint(0, 10)
    print(numero)
