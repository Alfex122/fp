Capital = int(input("Ingresar cantidad a invertir; $"))
Interes = int(input("Ingresar interes anual; %"))
Año = int(input("Ingresar años a invertir; "))

X = Interes/100
Z = Capital*X
M = Capital+Z
N = M*Año

print("Capital final a obtener; $",N)
print("Finalizado")