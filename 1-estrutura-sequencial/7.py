#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Informe o valor do lado do quadrado em (cm): "))

area = lado ** 2

print(f"Um quadrado com os lados valendo {lado}cm tem uma área de {area}cm com o dobro da area {2 * area}cm")