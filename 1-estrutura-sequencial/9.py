# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)

print(f"A temperatura {fahrenheit:.1f}°F para celsius é {celsius:.1f}°C")