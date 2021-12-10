#Area de figuras
##Alexis David Zambrano Ibarra

print("¿De que figura deseas obtener el area?")
print("1 = Circulo")
print("2 = Cuadrado")
print("3 = Rectangulo")
print("4 = Triangulo")
A = int(input("Ingresar numero; "))

if A == 1:
	Cir = int(input("Ingresar radio; "))
	R = Cir**2
	Ac = 3.1416 * R
	print("El area del circulo es; ", Ac)
elif A == 2:
	Cua = int(input("Ingresar el valor de un lado; "))
	print("El area del cuadrado es; ", Cua**2)
elif A == 3:
	Br = int(input("Ingresar el valor de la base; "))
	Lr = int(input("Ingresar el valor de la altura; "))
	print("El area del rectangulo es; ", Br*Lr)
elif A == 4:
	Bt = int(input("Ingresar el valor de la base; "))
	Ht = int(input("Ingresar el valor de la altura; "))
	print("El area del triangulo es; ", (Bt*Ht)/2)
else:
	print("Error")

print("Finalizado")