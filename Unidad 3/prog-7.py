#Imprimir numero mayor

N1 = int(input("Ingresar primer valor: "))
N2 = int(input("Ingresar segundo valor: "))

if N1 < N2:
	print (N2)
elif N1 > N2:
	print(N1)
else:
	print("Error: Datos incorrectos")

print("Finalizado")