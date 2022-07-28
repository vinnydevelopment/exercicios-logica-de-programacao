# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil

area = float(input("Informe o tamnho em metros quadrados da área a ser pintada: "))
tipo = int(input("Escolha entre Latas de 18 litros, Galões de 3,6 litros ou mesclado:[1][2][3] "))

litro = area / 6

if tipo == 1:
	#lata
	lata = ceil(litro / 18)
	preco = lata * 80
	print(f"Com uma parede de {area:.1f}m² é necessario {lata} latas, com o preço total de R${preco:.2f}")
elif tipo == 2:
	#galão
	galao = ceil(litro / 3.6)
	preco = galao * 25
	print(f"\nCom uma parede de {area:.1f}m² é necessario {galao} latas, com o preço total de R${preco:.2f}")
elif tipo == 3:
	#mesclado
	litro = (litro * 0.10) + litro
	qt_lata = 0
	qt_galao = 0
	#descobre a quantidade de latas
	while litro >= 18:
		lata = ceil(litro / 18)
		qt_lata += 1
		litro -= 18
	#descobre a quantidade de galões
	while litro > 0:
		galao = ceil(litro / 3.6)
		qt_galao += 1
		litro -= 3.6
	#preco total
	preco = (qt_lata * 80) + (qt_galao * 25)
	print(f"\nCom uma parede de {area:.1f}m² é necessario {qt_galao} galões e {qt_lata} latas, com o preço total de R${preco:.2f}")
else:
	print("escolha um tipo")
