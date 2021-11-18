class AlumnosT():
	def __init__(self, Edad, calM, calC, calFI, calFP, calT, calE, calI, Prom, CalPre, Resid):
		self.Edad = Edad
		self.Nombre = Nombre
		self.calM = calM
		self.calC = calC
		self.calFI = calFI
		self.calFP = calFP
		self.calT = calT
		self.calE = calE
		self.calI = calI
		self.CalPre = CalPre
		self.Prom = Prom
		self.Resid = Resid
		self.Dist= Dist

Reyna = AlumnosT(18, "Reyna", 6, 7, 5, 10, 8, 5, 9, 9, 7.14, "Emiliano Zapata", 13)
Mirozlava = AlumnosT(18,"Mirozalva",9, 8, 10, 7, 9, 6, 7, 8, 8, "Cosio", 27)
Melani = Alumnos(18,"Melany", 7, 8, 7, 5, 9, 10, 7, 7.51, 9, "pabellon", 5)
Diego = Alumnot(19,"Diego", 8, 9, 9, 10, 8, 8, 10, 8.85, 10, "rincón", 13) 
Britzy = AlumnosT(18,"Britzy", 10, 9, 10, 10, 8, 8, 10, 9.28, 10, "rincón", 13) 
Fernando = AlumnosT(17, "Fernando", 8, 8, 7, 9, 10, 8, 10, 8.57, 9, "pabellon", 5)
Alejandra = AlumnosT(18,"Alejandra", 10, 10, 10, 10, 10, 10, 10, 10, 8, "jesus maria", 27)
Alejandro= AlumnosT(19, "Alejandro", 10, 9, 8, 9, 8, 9, 8, 9, "Ejido Fresnillo", 17)
Donaldo= AlumnosT(18, "Donaldo", 8, 9, 10, 9, 8, 6, 8, 8.71, 8, "San Jose de Gracia", 18)
Austin= AlumnosT(18, "Austin", 10, 9, 8, 9, 10, 9, 8, 9, 8, "pabellon", 5)
Paola=AlumnosT(18,"Paola", 10, 9, 8, 9, 10, 9, 8, 9, 8, "carboneras", 8)
Isaac=AlumnosT(19, "Isaac", 10, 9, 10, 9, 10, 10, 10, 9.71, 9, "rincon", 13)
Areli=AlumnosT(19, "Areli", 10, 9, 10, 9, 10, 9, 10, 9.57, 8, "rincon", 13)
Elias=AlumnosT(18, "Elias", 10, 9, 10, 9, 10, 9, 10, 9.57, 8, "asientos", 11)
Alexis=AlumnosT(19, "Alexis", 10, 9, 10, 8, 7, 8, 7, 8.42, 8, "rincon", 13)

p = (Reyna.calFP+Mirozlava.calFP+Melani.calFP+Diego.calFP+Britzy.calFP+Fernando.calFP+Alejandra.calFP+
	Alejandro.calFP+Donaldo.calFP+Austin.calFP+Paola.calFP+Isaac.calFP+Areli.calFP+Elias.calFP+Alexis.calFP)/15

print("Alumnos mayores: ", Alexis.Edad," ", Areli.Edad," ",Alejandro.Edad," ",Diego.Edad," ",Isaac.Edad)
print("Promedios obtenidos en preparatoria: ",Reyna.Nombre, ": ",Reyna.Prom, "   ",Mirozlava.Nombre, ": ", Mirozlava.Prom, "   ",
	Melani.Nombre, ": ", Melani.Prom, "   ", Diego.Nombre, ": ", Diego.Prom, "   ", Britzy.Nombre, ": ", Britzy.Prom, "   ", 
	Fernando.Nombre, ": ", Fernando.Prom, "   ", Alejandra.Nombre, ": ", Alejandra.Prom,"   ", Alejandro.Nombre, ": ", 
	Alejandro.Prom, "   ", Donaldo.Nombre, ": ", Donaldo.Prom,"   ", Austin.Nombre, ": ", Austin.Prom, "   ", 
	Paola.Nombre, ": ", Paola.Prom, "   ", Isaac.Nombre, ": ", Isaac.Prom, "   ", Areli.Nombre, ": ", Areli.Prom, "   ", 
	Elias.Nombre, ": ", Elias.Prom, "   ", Alexis.Nombre, ": ", Alexis.Prom)

print("El alumno que vive mas lejos es; ", Mirozlava.Nombre, "es de ", Mirozlava.Resid, "con una distancia de ", Mirozlava.Dist, "Km")
print("El alumno que vive mas cerca es; ", Melani.Nombre, "es de ", Melani.Resid, "con una distancia de ", Melani.Dist, "Km")

print("La materia con mayor rendimiento es Fundamentos de Programacion con un promedio de; ", P )

print("Finalizado")