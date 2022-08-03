# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Informe o seu sexo feminino ou masculino:[F][M] ").lower()

if letra == "f":
	print("Seu sexo é feminino")
elif letra == "m":
	print("Seu sexo é masculino")
else:
	print("Sexo Inválido")