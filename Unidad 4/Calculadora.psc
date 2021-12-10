Algoritmo Calculadora
	Escribir "Calculadora"
	Escribir "Que desea hacer?"
	Escribir "1=Sumar	 2=Restar 		3=Multiplicar  		4=Dividir"
	Leer X 
	Escribir "Ingresa el primer valor; "
	Leer Num1
	Escribir "Ingresa el segundo valor; "
	Leer Num2
	R1 = Num1+Num2
	R2 = Num1*Num2
	R3 = Num1-Num2
	R4 = Num1/Num2
		Segun x Hacer
			1:
				Imprimir  "Resultado; ", R1
			3:
				Imprimir "Resultado; ", R3
			2:
				Imprimir "Resultado; ", R2
			4:
				Imprimir "Resultado; ", R4
			De Otro Modo:
				Imprimir "Error"
		Fin Segun	
FinAlgoritmo
