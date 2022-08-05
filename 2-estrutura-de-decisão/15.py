# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = int(input("Informe o valor do lado A: "))
b = int(input("Informe o valor do lado B: "))
c = int(input("Informe o valor do lado C: "))

somaAB = a + b
somaAC = a + c
somaBC = b + c


if somaAB >= c and somaAC >= b and somaBC >= a:
	if a == b and a == c:
		tipo = "triângulo equilátero"
	elif b == c or a == b or a == c:
		tipo = "triângulo Isósceles"
	else:
		tipo = "triângulo escaleno"
else:
	print("Não é um triângulo")

print(f"\n{tipo.title()}")