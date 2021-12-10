Algoritmo NombreAleatorio
	Definir num Como Entero
	Definir Nom, N Como Caracter
	Escribir "Ingresar nombre"
	leer Nom
	num = Longitud(Nom)
	N = ""
	mientras num > 1 Hacer
		N = N +Subcadena(Nom, num, num)
		num = azar(30)
	FinMientras
	Imprimir "El nombre es; " Nom " de forma aleatoria; " N
FinAlgoritmo
