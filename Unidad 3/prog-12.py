#Imprimir la persona mayor
N1 = input("Ingresar nombre; ")
E1 = int(input("Ingresar su edad; "))
N2 = input("Ingresar nombre; ")
E2 = int(input("Ingresar su edad; "))

if E1 > E2:
	print(N1,E1)
elif E1 < E2:
	print(N2, E2)
else:
	print("Error")

print("Finalizado")