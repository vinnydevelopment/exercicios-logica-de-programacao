# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe sua altura: "))

homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

print(f"Para um HOMEM de altura {altura:.2f}m o peso ideal é {homem:.2f}kg")
print(f"Para uma MULHER de altura {altura:.2f}m o peso ideal é {mulher:.2f}kg")