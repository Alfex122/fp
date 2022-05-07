class Consolas:
    Año = 0
    Color = ""
    Marca = "" 
    Generación = 0
print(("¬°¬") * 20)
print("Ing. Alexis David Zambrano Ibarra")
print("Ing. Alejandro Herrera Ramos")
print("Ing. Diego Armando Garcia Castillo")
print("Ing. Fernando Ulises Gomez Sanchez")
print("")
print("----Metodos----")
print("Sort")
print("Push")
print("Index")
print("")
print("----Atributos----")
print("Año")
print("Color")
print("Marca")
print("Generación")
print("Presiona enter para continuar"))
print(("¬°¬") * 20)
A = str(input())
Imprimir = []
Nombre = []
Nom = []
año = []
color = []
marca = []
generación = []
Heidis = []
for i in range (10):
    print("Ingresar el nombre del objeto ", (i+1), " junto con los atributos")
    V = str(input("; "))
    Nombre.append(V)
    Nom.append(V)
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
print("3 == Index")
Menu=int(input("¿Que tipo de acomodo quieres?; "))
if Menu == 1:
    print("--Metodo Sort--")
    print("Quieres acomodar los objetos por año ó por generación")
    print("1 == Año")
    print("2 == Generación")
    Selector=int(input("Ingresa el numero de la opcion; "))
    if Selector == 1:
        qs = sorted(año)
        Ara = True
        contador = 0  
        print("La lista ordenada por Año es la siguiente; ")
        while Ara:
            for i in range (10):
                if qs[contador] == año[i]:
                    a = ["Nombre; ", Nom[i], "Año; ", año[i], "Color; ", color[i], "Marca; ", marca[i], "Generación; ", generación[i]]
                    print(a)
                    Heidis.append(a)
            contador = contador + 1
            if contador == 10:
                Ara = False
        print("Finalizado")
    elif Selector == 2:
        qs = sorted(generación)
        Ara = True
        contador = 0  
        print("La lista ordenada por Generación es la siguiente; ")
        while Ara:
            for i in range (10):
                if qs[contador] == generación[i]:
                    a = ["Nombre; ", Nom[i], "Año; ", año[i], "Color; ", color[i], "Marca; ", marca[i], "Generación; ", generación[i]]
                    print(a)
                    Heidis.append(a)
            contador = contador + 1
            if contador == 10:
                Ara = False
        print("Finalizado")
    else:
        print("Error, la opcion seleccionada no esta en el parametro")
        for i in range(10):
            print("Nombre; ", Nom[i], "Año; ", año[i], "Color; ", color[i], "Marca; ", marca[i], "Generación; ", generación[i])
            print("Finalizado")
elif Menu == 2:
    pass#Falta la parte de alejandro aqui 
elif Menu == 3:
    print("--Metodo Reverse--")
    print("La lista ordenada es la siguiente; ")
    a = []
    b = []
    c = []
    d = []
    e = []
    for i in range (10):
        b.append("Año: ")
        b.append(Heidis[i].Año)
        a.append(b)
        c.append("Color: ")
        c.append(Heidis[i].Color)
        a.append(c)
        d.append("Marca: ")
        d.append(Heidis[i].Marca)
        a.append(d)
        e.append("Generacion: ")
        e.append(Heidis[i].Generación)
        a.append(e)
        a.reverse()
        print(a)
    print("Finalizado")
else:
    print("Opcion ingresada no es valida")
    for i in range (10):
        print("Nombre; ", Nom[i], "Año; ", año[i], "Color; ", color[i], "Marca; ", marca[i], "Generación; ", generación[i])
    print("Finalizado")