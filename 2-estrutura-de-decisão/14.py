# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Informe a primeira nota [0-10]: "))
nota2 = float(input("Informe a segunda nota [0-10]: "))

media = (nota1 + nota2) / 2

if media > 9 and media <= 10:
	conceito = 'a'
elif media > 7.5:
	conceito = 'b'
elif media > 6:
	conceito = 'c'
elif media > 4:
	conceito = 'd'
else:
	conceito = 'e'

if conceito == 'a' or conceito == 'b' or conceito == 'c':
	situacao = "aprovado"
else:
	situacao = "reprovado"

print(f"\nPrimeira nota: {nota1:2.1f}")
print(f"Segunda nota: {nota2:2.1f}")
print(f"Média: {media:2.1f}")
print(f"Conceito: {conceito.upper()}")
print(f"Situação: {situacao.title()}")