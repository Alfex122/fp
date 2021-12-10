Algoritmo Area
	Escribir "¿De que figura deseas obtener el area?"
	Escribir "1 = Circulo"
	Escribir "2 = Cuadrado"
	Escribir "3 = Rectangulo"
	Escribir "4 = Triangulo"
	leer A
	Segun A Hacer
		1:
			Escribir "Ingresar radio"
			Leer Cir
			R = cir^2
			Ac = 3.1416 * R
			Imprimir "El area del circulo es; ", Ac
		2:
			Escribir "ingresar el valor de un lado"
			Leer Cua
			Escribir "El area del cuadrado es; ", Cua^2
		3:
			Escribir "Ingresar el valor de la base"
			Leer Br
			Escribir "Ingresar el valor de la altura"
			Leer Lr
			Escribir "El area del rectangulo es; ", Br*Lr
		4:
			Escribir "Ingresar el valor de la base"
			Leer Bt
			Escribir "Ingresar el valor de la altura"
			Leer Ht
			Imprimir "El area del triangulo es; ", (Bt*Ht)/2
	FinSegun
FinAlgoritmo
