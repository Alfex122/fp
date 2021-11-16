#pedir 5 calificaciones y obtener promedio
Nombre = input("Ingresar nombre: ")
l = ("Escibir calificaciones")
C = int(input("Calculo: "))
M = int(input("Matematicas: "))
I = int(input("Ingles: "))
P = int(input("Programacion: "))
T = int(input("TICS: "))

Cal = (C+M+I+P+T)
Prom = Cal/5

print(Prom)
print("Finalizado")