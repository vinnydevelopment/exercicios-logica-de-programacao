# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite um número: "))

if numero == 1:
	dia = "Domingo"
elif numero == 2:
	dia = "Segunda"
elif numero == 3:
	dia = "Terça"
elif numero == 4:
	dia = "Quarta"
elif numero == 5:
	dia = "Quinta"
elif numero == 6:
	dia = "Sexta"
elif numero == 7:
	dia = "Sábado"
else:
	dia = "Valor inválido"

print(dia)