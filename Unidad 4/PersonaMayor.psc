Algoritmo ImprimirLaPersonaMayor 
	Escribir "Ingresar el primer nombre; "
	Leer N1
	Escribir "Ingresar el segundo nombre; "
	Leer N2
	X = Longitud(N1)
	N = Longitud(N2)
	Si Longitud(N1) > Longitud(N2) Entonces
		Imprimir "La cantidad de caracteres que tiene el nombre mas largo son; ", X
		Imprimir "El nombre es; ", N1 
	SiNo
		Imprimir "La cantidad de caracteres que tiene el nombre mas largo son; ", N
		Imprimir "El nombre es; ", N2
	Fin Si
FinAlgoritmo
