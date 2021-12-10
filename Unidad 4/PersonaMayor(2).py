#Imprimir a la persona mayor
##Alexis David Zambrano Ibarra

N1 = input("Ingresar el primer nombre; ")
N2 = input("Ingresar el segundo nombre; ")
X = len(N1)
N = len(N2)

if len(N1)>len(N2):
	print("La cantidad de caracteres que tiene el nombre mas largo es; ", X)
	print("El nombre es; ", N1)
elif len(N1)<len(N2):
	print("La cantidad de caracteres que tiene el nombre mas largo es; ", N)
	print("El nombre es; ", N2)
else:
	print("Error")

print("Finalizado")