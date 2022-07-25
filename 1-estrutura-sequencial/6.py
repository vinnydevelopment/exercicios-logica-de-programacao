#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("informe o valor do raio em centimentros: "))
PI = 3.14

area = PI * raio ** 2

print(f"A área de um círculo de raio {raio:.1f}cm é igual a {area:.1f}cm")