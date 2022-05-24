class Telefono:
    Marca = "Samsung"
    Modelo = "S10"
    Bateria = "Litio"
    CapacidadBateria = 3700
    Memoria = 128
    Ram = 8
    Color = "Blanco"
    Wifi = True
    Bluethoot = True 
    Carga = 100

    def Conexion(self):
        if self.Wifi == False:
            print("El dispositivo esta desconectado")
        else:
            print("El dispositivo esta conectado")
        
    def Transferencia(self):
        if self.Bluethoot == True:
            print("El dispositivo puede transferir archivos")
        else:
            print("El dispositivo no puede transferir archivos, active la conexion bluethoot")

    def Cargando(self):
        if self.Carga == 100:
            print("El telefono esta cargado completamente")
        elif self.Carga > 20:
            print("Esta cargado")
        else:
            print("El dispositivo esta descargado, Conecte el cargador")

Motorola = Telefono()
Motorola.Marca="Motorola"
Motorola.Modelo="G60"
Motorola.Bateria
Motorola.CapacidadBateria=4500
Motorola.Memoria =64
Motorola.Ram = 4
Motorola.Color = "Azul"
Motorola.Wifi
Motorola.Bluethoot =False
Motorola.Carga = 85

Xiaomi = Telefono ()
Xiaomi.Marca="Xiaomi"
Xiaomi.Modelo="Poco X3"
Xiaomi.Bateria
Xiaomi.CapacidadBateria=4800
Xiaomi.Memoria = 256
Xiaomi.Ram
Xiaomi.Color="Negro"
Xiaomi.Wifi
Xiaomi.Bluethoot
Xiaomi.Carga=54