Algoritmo Numero_Fibonacci
	Escribir "Dame un numero: "
	Leer NF
	Definir x Como Entero
	Definir a,b,c Como Real
	a = 0
	b = 1 
	C = 1
	Mientras x<=NF Hacer
		
		Escribir a
		c = a + b
		a = b
		b = c
		x= x+ 1
	FinMientras
	Z = x + b - x-1
	Escribir "Resultado: ", Z
	
FinAlgoritmo
