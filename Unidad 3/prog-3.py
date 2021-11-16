#Imprimir 5 calificaciones en un renglon
Nombre = input("Ingresar nombre: ")
notas = dict()

notas["Calculo: "] = int(input("Calculo"))
notas["matematicas"] = int(input("Matematica: "))
notas["ingles"] = int(input("Ingles: "))
notas["programacion"] = int(input("Programacion: "))
notas["TICS"] = int(input("TICS: "))

print(notas)
print("Finalizado")