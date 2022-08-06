# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from math import sqrt

a = int(input("Informe o valor A: "))
if a == 0:
	print("Essa equação não é de segundo grau")
else:
	b = int(input("Informe o valor B: "))
	c = int(input("Informe o valor C: "))
	x = 2

	delta = b**2 - 4 * a * c

	if delta < 0:
		print(f"\nO delta {delta} é negativo, essa equação não possui raizes reais")
	elif delta > 0:
		delta = sqrt(delta)
		raiz_real1 = (-b + delta) / (2 * a) 
		raiz_real2 = (-b - delta) / (2 * a)
		print(f"\nraiz real 1: {raiz_real1}")
		print(f"raiz real 2: {raiz_real2}")
	else:
		raiz_real = -b / (2 * a) 
		print(f"\nraiz real: {raiz_real}")
	
