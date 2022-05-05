class Consolas:
    Año = 0
    Color = ""
    Marca = "" 
    Generación = 0
print("¬°¬") * 20
print("Ing. Alexis David Zambrano Ibarra")
print("Ing. Alejandro Herrera Ramos")
print("Ing. Diego Armando Garcia Castillo")
print("Ing. Fernando Ulises Gomez Sanchez")
print("")
print("----Metodos----")
print("Sort")
print("Push")
print("Append")
print("")
print("----Atributos----")
print("Año")
print("Color")
print("Marca")
print("Generación")
A = str(input("Presiona enter para continuar"))
print("¬°¬") * 20
Nombre = []
año = []
color = []
marca = []
generación = []
Heidis = []
for i in range (10):
    print("Ingresar el nombre del objeto ", (i+1), " junto con los atributos")
    V = str(input("; "))
    Nombre.append(V)
    W = int(input("Año de fabricación; "))
    año.append(W)
    X = str(input("Color; "))
    color.append(X)
    Y = str(input("Marca; "))
    marca.append(Y)
    Z = int(input("Generación; "))
    generación.append(Z)
for x in range (10):
    Nombre[x] = Consolas ()
    Nombre[x].Año = año[x]
    Nombre[x].Color = color[x]
    Nombre[x].Marca = marca[x]
    Nombre[x].Generación = generación[x]
    Heidis.append(Nombre[x])
print("Metodos de acomodo")
print("1 == Sort")
print("2 == Push")
print("3 == Append")
Menu=int(input("¿Que tipo de acomodo quieres?; "))