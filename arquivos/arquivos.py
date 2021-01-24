
# Abre o arquivo
arquivo = open("arquivos/arquivo.txt")


# Readlines
linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

# Read
texto_completo = arquivo.read()

# print(texto_completo)

# Readline
linha_unica = arquivo.readline()

print(linha_unica)


arquivo_novo = open("arquivos/arquivo2.txt", "w")

arquivo_novo.write("Esse eh meu arquivo 2!")
arquivo_novo.close()
