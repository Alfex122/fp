Algoritmo ImprimirElNumeroMayor
	Escribir "Dame el primer valor"
	Leer N1
	Escribir "Dame el segundo valor"
	Leer N2
	Escribir "Dame el tercer valor"
	Leer N
	Si N1>N2 O N1>N3 Entonces
		Escribir N1
	SiNo
		Si N2>N1 O N2>N Entonces
			Escribir N2
		SiNo
			Si N>N1 O N>N2 Entonces
				Escribir N
			SiNo
				Escribir "Todos los valores son iguaes"
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
