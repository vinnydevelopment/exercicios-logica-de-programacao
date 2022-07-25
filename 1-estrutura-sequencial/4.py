#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Nota 1ª bimestre: "))
nota2 = float(input("Nota 2ª bimestre: "))
nota3 = float(input("Nota 3ª bimestre: "))
nota4 = float(input("Nota 4ª bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média anual foi {media:.1f}")