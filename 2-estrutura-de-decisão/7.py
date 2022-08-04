# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
	maior = num1
	menor = num1
else:
	menor = num1
if num2 > num1 and num2 > num3:
 	maior = num2
else:
#elif num2 < menor:
 	menor = num2
if num3 > num1 and num3 > num2:
 	maior = num3
else:
#elif num3 < menor:
	menor = num3

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
