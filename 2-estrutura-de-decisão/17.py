# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Informe um ano e descubra se ele é bissexto: "))

# divisivel por 4 e não divisivel por 100 ou divisivel por 100 e 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0):
	print(f"\n{ano} é um ano bissexto")
else:
	print(f"\n{ano} é um ano normal")
