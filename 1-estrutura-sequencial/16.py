# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil

area = float(input("Informe o tamnho em metros quadrados da área a ser pintada: "))

litro = area / 3
lata = ceil(litro / 18)
preco = lata * 80

print(f"Para uma parede de {area:.1f}m² é necessario {lata} latas de tinta, o preço total é R${preco:.2f}")
