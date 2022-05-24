class Animales:
    Tipo = "Acuatico"
    Habitat = "Mar Caribe"
    Movimiento = "Nada"
    Grupo = "Carnivoro"
    NumExtremidades = 4
    Sonido = "No genera"
    Peso = 775
    Velocidad = 56
    EdadAprox = 70

    def Alimento(self):
        return self.Grupo

    def Cazar(self):
        if self.Alimento() != "Herviboro":
            print ("El animal puede cazar")
        else:
            print("El animal no caza por que es herviboro")

    def Rugir(self):
        print(self.Sonido)

Leon = Animales()
Leon.Tipo = "Terrestre"
Leon.Habitat = "Savana"
Leon.Movimiento = "Camina/Corre"
Leon.Grupo
Leon.NumExtremidades = 5
Leon.Sonido= "Ruge"
Leon.Peso = 600
Leon.Velocidad = 45
Leon.EdadAprox = 35
print(Leon.EdadAprox)

Tiburon = Animales()
Tiburon.Tipo= "Acuatico"
Tiburon.Habitat = "Agua Salada"
Tiburon.Movimiento="Nadar"
Tiburon.Grupo
Tiburon.NumExtremidades=4
Tiburon.Sonido = ""
Tiburon.Peso=250
Tiburon.Velocidad=35
Tiburon.EdadAprox = 70