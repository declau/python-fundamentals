# Função enumerate, navegar na lista e ao mesmo tempo obter o indice de cada elemento

lista = ["Bola", "Banana", "tenis"]

for i in range(len(lista)):
    print(i, lista[i])

# Pytonico
print("-------------------")
for i, nome in enumerate(lista):
    print(i, nome)
