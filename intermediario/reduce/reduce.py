from functools import reduce

# Reduce, recebe uma lista e retona um unico valor


def soma(x, y):
    return x + y


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_total = reduce(soma, lista)  # soma todos os valores da lita
print(soma_total)
