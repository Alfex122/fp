#Nombre aleatorio
##Alexis David Zambrano Ibarra

Nom = input("Ingresar el nombre; ")
num = len(Nom)

import string, random
N = string.ascii_letters

if __name__ == '__main__':
	rstr = random.choice(string.ascii_letters)

	print("El nombre es;", Nom)
	print("El nombre aleatorio es; ", (rstr*(len(Nom))))
	
print("Finalizado")