# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Informe o preço do 1° produto: R$"))
produto2 = float(input("Informe o preço do 2° produto: R$"))
produto3 = float(input("Informe o preço do 3° produto: R$"))

if (produto1 < produto2) and (produto1 < produto3):
	comprar = "1° produto"
elif (produto2 < produto3):
	comprar = "2° produto"
else:
	comprar = "3° produto"

print(f"Você deve compra o {comprar}")