Algoritmo AprobadoReprobado
	N <- 5
	Escribir "Dame las calificaciones"
	Leer C1
	Leer C2
	Leer C3
	Leer C4
	Leer C5
	Cal <- C1+C2+C3+C4+C5
	Prom <- (Cal/N)
	Si Prom < 7 Entonces
		Escribir (Prom), " " ("Reprobado")
	SiNo
		Escribir (Prom), " " ("Aprobado")
	Fin Si
	
FinAlgoritmo
