numero = 7
running = True

while running:
	Nombre = input ("Ingresar el nombre del alumno: ")
	Cal = int (input ("Ingresar la calificacion obtenida: "))

	if Cal > numero:
		print (Nombre) 
		print ("Aprobo")
	elif Cal <= numero:
		print(Nombre)
		print("Reprobo")
	else:
		print(Nombre, "Reprobo")
else:
	print("El bucle finalizo")

print("Finalizado")