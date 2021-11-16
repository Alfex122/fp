#Imprimir el numero mayor
X = int(input("Primer valor: "))
Y = int(input("Segundo valor: "))
Z = int(input("Tercer valor: "))

if X > Y and Z:
	print(X)
elif Y > X and Z:
		print(Y)
elif Z > X and Y:
		print(Z)
else:
		print("Error")

print("Finalizado")