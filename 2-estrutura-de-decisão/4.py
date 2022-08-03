# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a', 'e', 'i', 'o', 'u']
#caso queira verificar todas as letras usar o loop for com a lista alfabeto
# alfabeto = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'x', 'z']

letra = input("Informe uma letra: ").lower()

if letra in vogais:
	print(f"a letra {letra.upper()} é uma vogal")
else:
	print(f"a letra {letra.upper()} é uma consoante")