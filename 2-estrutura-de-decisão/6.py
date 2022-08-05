# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
	maior = num1
	print(f"O maior número é {maior}")
elif num2 > num3:
	maior =  num2
	print(f"O maior número é {maior}")
elif num3 > num1:
	maior = num3
	print(f"O maior número é {maior}")
else:
	print("Ambos são iguais")
