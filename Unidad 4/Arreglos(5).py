#Clase y atributo y guardarlos en un arreglo 
##Alexis David Zambrano Ibarra

Cla = input("Ingresar el nombre de la clase; ")
class programacion:
	"""docstring for ClassName"""
	def __init__(self, C1, C2, C3, C4, C5):
		self.C1 = C1 
		self.C2 = C2
		self.C3 = C3
		self.C4 = C4
		self.C5 = C5

A = input("Ingresar el primer atributo; ")
B = input("Ingresar el segundo atributo; ")
C = input("Ingresar el tercer atributo; ")
D = input("Ingresar el ciarto atributo; ")
E = input("Ingresar el quinto atributo; ")
cl1 = programacion(A, B, C, D, E)

Array = [cl1.C1, cl1.C2, cl1.C3, cl1.C4, cl1.C5]
print("El nombre de la clase es; ", Cla)
print("Sus atributos son; ",Array)