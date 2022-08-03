# Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

if num1 > num2:
	print(f"O maior número é {num1}\n")
elif num2 > num1:
	print(f"O maior número é {num2}\n")
else:
	print("Os números são iguais\n")