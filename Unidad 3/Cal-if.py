Promedio = 7
Nombre = input ("Ingresar el nombre del alumno: ")
Cal = int (input ("Ingresar la calificacion obtenida: "))

if Cal > Promedio:
	print (Nombre) 
	print ("Aprobo")
elif Cal < Promedio:
	print(Nombre)
	print("Reprobo")
else:
	print("Error: calificacion no valida")

print("Finalizado")