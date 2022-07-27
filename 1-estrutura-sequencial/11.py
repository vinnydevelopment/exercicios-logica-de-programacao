# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

primeiro = int(input("Informe o primeiro (inteiro):"))
segundo = int(input("Informe o segundo (inteiro): "))
terceiro = float(input("Informe o terceiro (real): "))

a = (primeiro * 2) * (segundo / 2)
b = (primeiro * 3) + terceiro
c = terceiro ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {a}")
print(f"A soma do triplo do primeiro com o terceiro: {b}")
print(f"O terceiro elevado ao cubo: {c}")