# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Informe o turno em que você estuda?")
turno = input("[ M ] - matutino\n[ V ] - Vespertino\n[ N ] - Norturno\n:").lower()

if turno == 'm':
	print("Bom Dia!")
elif turno == 'v':
	print("Boa Tarde!")
elif turno == 'n':
	print("Boa Noite!")
else:
	print("Valor Inválido!")