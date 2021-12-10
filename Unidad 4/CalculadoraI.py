#Calculadora con interfaz grafica
##Alexis David Zambrano Ibarra

from tkinter import Tk,Text

Alejandra = Tk()

class Cal:
	def __init__ (self, reyna):
		self.reyna=reyna
		self.reyna.title("Calculadora")#pantalla
		self.reyna.iconbitmap("B1.ico")
		self.reyna.config(bg="Pink")
		self.reyna.config(bd=10)
		self.reyna.config(relief="groove")
		#crear frame
		#bg = color de fondo
		#font = tipo de fuente
		#fg = color de fuente
		#configuracion del fondo, tipo de fuente y color de fuente
		#Ubicar pantalla en la ventana
		#row=fila, column=columna, columspand=numero de columnas(empieza en la columna "0"), pad=relleno de los bordes(X=izq,derecha, Y=arriba,abajo)
		#ancho del cuadro
		self.isaac=Text(reyna, state="disable", width=40, height=3, bg="Green", font=("Helvetica",15), fg="Black")
		self.isaac.grid(row=0, column=0, columnspan=4, padx=5, pady=5)#Variable
		self.isaac.config(bd=10, relief="sunken")
		#gurdar operacion en una variable, mientras mas se hagan operaciones se van a guardar en esta variable(debe de estar vacio para generar esto)
		self.mely=""

		#crear los botones
		Fernando1=self.Austin(1)
		Fernando2=self.Austin(2)
		Fernando3=self.Austin(3)
		Fernando4=self.Austin(4)
		Fernando5=self.Austin(5)
		Fernando6=self.Austin(6)
		Fernando7=self.Austin(7)
		Fernando8=self.Austin(8)
		Fernando9=self.Austin(9)
		Fernando10=self.Austin(0)
		Fernando11=self.Austin("+")
		Fernando12=self.Austin("*")
		Fernando13=self.Austin(".")
		Fernando14=self.Austin("-")
		Fernando15=self.Austin("=")
		Fernando16=self.Austin(u"/u232", escribir=False)
		Fernando17=self.Austin(u"/u00F7")

		#ubicar los botones en una arreglo
		Areli  = [Fernando1, Fernando2, Fernando3, Fernando4, Fernando5, Fernando6, Fernando7, Fernando8, Fernando9, Fernando10, Fernando11, Fernando12, Fernando13, Fernando14, Fernando15, Fernando16, Fernando17]
		britzy=0

		for fila in range (1, 5):
			for columna in range(4):
				Areli[britzy].grid(row=fila, column=columna)
		Areli[16].grid(row=5, column=0, columnspan=4)#

		returnfont=("Helvetica",15)


		def Austin(self,valor,escribir=True, ancho=1, alto=1):
			return Button(self, reyna, textr=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor, escribir))

Alejandro=Cal(Alejandra)
Alejandra.mainloop()
