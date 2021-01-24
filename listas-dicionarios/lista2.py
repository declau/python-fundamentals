# Ordenar lista
lista = [1, 0, 9, 77, 66, 55, 45, 32, 11]
print("lista", lista)
lista.sort()
print("Ordenada", lista)
# ordenar decrescente
lista.sort(reverse=True)
print("decrescente", lista)

# sorted retorna uma lista ordenada
lista2 = [1, 32, 45, 47, 78, 789, 654, 333, 23]
print("lista inicial:", lista2)
lista2 = sorted(lista2)
print("lista retornada:", lista2)

# rnverter as posições de uma lista pegando o último elemento e passando para primeiro
lista2.reverse()
print("Reverse", lista2)
