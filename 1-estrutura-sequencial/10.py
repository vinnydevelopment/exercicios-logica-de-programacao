#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Informe a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"A temperatura {celsius:.1f}°C para fahrenheit é {fahrenheit:.1f}°F")