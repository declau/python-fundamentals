# Zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate",  "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00", "R$ 1,00", "R$ 200,00", "R$ 100000,00", "R$ 1000.000,00"]

# zip vai compactar as duas listas como se fosse uma

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)

# output:
# 1 abacate R$ 2,00
# 2 bola R$ 1,00
# 3 cachorro R$ 200,00
# 4 dinheiro R$ 100000,00
# 5 elefante R$ 1000.000,00
