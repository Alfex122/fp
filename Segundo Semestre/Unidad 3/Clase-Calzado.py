class Calzado:
    Tipo = "Vestir"
    Medida = 27
    Marca = "Chabelo"
    Agujetas = False
    Color = "Negro"
    Fabricación = 2022

    def Proteger(self):
        return self.Medida
    
    def Amarrar(self):
        if self.Agujetas == True:
            print("El calzado se puede amarrar")
        else:
            print("El calzado no se puede amarrar por que no tiene agujetas")

    def Correr (self):
        return self.Tipo

    def Vestir (self):
        if self.Tipo() == "Tenis":
            print("El tipo de vestimenta puede ser deportivo o casual")
        else:
            print("El tipo de vestimenta puede ser casual o formal")

    def Usar (self):
        if self.Proteger < self.Proteger:
            print("El zapato es mas grande")
        elif self.Proteger > self.Proteger:
            print ("El calzado es mas chico")
        else: 
            print("El calzado es de la medida indicada")

Tenis = Calzado()
Tenis.Tipo = "Vestir/Deportivo"
Tenis.Medida
Tenis.Marca="Patito"
Tenis.Agujetas=True
Tenis.Color
Tenis.Fabricación = 2021

Zapatillas = Calzado()
Zapatillas.Tipo
Zapatillas.Medida = 25
Zapatillas.Marca = "Cenicienta"
Zapatillas.Agujetas
Zapatillas.Fabricación