class carro:
    color = "Azul"
    placas = "HED-0410"
    Alarma = True
    Cilindraje = 6
    Marca = "Mazda"
    Motor = 3.141592
    Año = 2020
    NumPuertas = 5
    
    def Desbloqueado(self):
        return self.Alarma
    
    def AbrirCarro(self):
        if self.Desbloqueado() == False:
            print("El carro esta bloqueado")
            print("* Suena el carro *")
        
        else:
            print("El carro esta abierto")

Deportivo = carro()
Deportivo.color = "Gris"
Deportivo.placas ="AAA-4048"
Deportivo.Alarma
Deportivo.Cilindraje = 8
Deportivo.Marca="Mercedez"
Deportivo.Motor = 2.8
Deportivo.Año
Deportivo.NumPuertas = 3

Terreno= carro()
Terreno.color="Negro"
Terreno.placas
Terreno.Alarma=False
Terreno.Cilindraje
Terreno.Marca="Nissan"
Terreno.Motor = 3
Terreno.Año = 2022
Terreno.NumPuertas = 4