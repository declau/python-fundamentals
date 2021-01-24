minha_lista = ["dedo", "Dunha", "dinda"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = [1, "Denis", 2.23, "Tito", True]

print(minha_lista)
# Percorrendo uma lista com for
for item in minha_lista3:
    print(item)


# Tamanho da Lista
tamanho = len(minha_lista2)
print("Tamanho", tamanho)


# Pega o index 2 da Lista
print(minha_lista[2])

minha_lista.append("Dartanha")
print(minha_lista)

# verifica se elemento esta na lista
if 7 in minha_lista2:
    print("3 esta na lista")
else:
    print("Nao esta na lista")


# Remover item da lista
del minha_lista[3]
print(minha_lista)
# Remove a partir do index 1
del minha_lista[1:]
print(minha_lista)
# Remove todos os itens da lista
del minha_lista[:]
print(minha_lista)
