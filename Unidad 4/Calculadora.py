#Calculadora 
##Alexis David Zambrano Ibarra

print("Calculadora")
running = True

while running:
	print("1=Sumar 		2=Restar 	3=Multiplicar 	4=Dividir")
	X = int(input("¿Que deseas hacer?"))
	if X == 1:
		Num1 = int(input("Ingresar el primer valor; "))
		Num2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", Num1+Num2)
	elif X == 3:
		Num1 = int(input("Ingresar el primer valor; "))
		Num2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", Num1*Num2)
	elif X == 2:
		Num1 = int(input("Ingresar el primer valor; "))
		Num2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", Num1-Num2)
	elif X == 4:
		Num1 = int(input("Ingresar el primer valor; "))
		Num2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", Num1/Num2)
	elif X == 5:
		print("Error")
else:
	print("Fin")

print("Finalizado")