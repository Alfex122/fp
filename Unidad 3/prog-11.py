#Pedir calificaciones y que muestre si aprobo
N = 5
Nombre = input("Ingresar nombre: ")
print("Ingresar calificaciones: ")
C1 = int(input("Matematicas: "))
C2 = int(input("Programacion: "))
C3 = int(input("Ingles: "))
C4 = int(input("TICS: "))
C5 = int(input("Calculo: "))

Cal = (C1+C2+C3+C4+C5)
Prom = (Cal/N)

if Prom > 7:
	print(Nombre, Prom, " Aprobo")
elif Prom < 7:
	print(Nombre, Prom, " Reprobo")
else:
	print("Error")

print("Finalizado")