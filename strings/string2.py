upper_case = "denis"

print(upper_case.upper())

lower_case = "DENIS"
especial = "quebra de linha" + "\n"

print(especial.strip())  # retira caracteres especiais
print(lower_case.lower())


minha_string = "O rato roeu a roupa do rei de Roma"
minha_string = minha_string.replace("rei", "rainha")
print(minha_string)
minha_lista = minha_string.split()  # converte para uma lista
print(minha_lista)


seq = "CTA CTA CTA CTA CCT CTA CTA CCT"
busca = seq.find("CCT")  # mostra o indice da palavra
print(busca)
