# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Informe o 1° número: "))
num2 = int(input("Informe o 2° número: "))
num3 = int(input("Informe o 3° número: "))

if (num1 > num2) and (num1 > num3):
	primeiro = num1
	if (num2 > num3):
		segundo = num2
		terceiro = num3
	else:
		segundo = num3
		terceiro = num2
elif (num2 > num3):
	primeiro = num2
	if (num1 > num3):
		segundo = num1
		terceiro = num3
	else:
		segundo = num3
		terceiro = num1
else:
	primeiro = num3
	if (num1 > num2):
		segundo = num1
		terceiro = num2
	else:
		segundo = num2
		terceiro = num1


print(f"{primeiro}, {segundo}, {terceiro}")