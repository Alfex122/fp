Algoritmo ImprimirNombreMasLargo
	Escribir "Dame el primer nombre"
	Leer First
	First <- Mayusculas(First)
	Escribir "Dame el segundo nombre"
	Leer Second
	Second <- Mayusculas(Second)
	si Longitud(First) > Longitud(Second) Entonces
		Escribir First
	sino 
		Escribir Second
	FinSi
	
FinAlgoritmo
