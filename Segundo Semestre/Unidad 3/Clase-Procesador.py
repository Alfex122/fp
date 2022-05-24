class Procesador:
    Nucleos = 4
    Generación = 10
    SubProcesos = 8
    Marca = "AMD"
    Linea = "Ryzen"
    Modelo = 5
    AltaGama = True

    def Velocidad(self):
        if self.SubProcesos > 3:
            print("El microprocesador es rapido")
        else:
            print("El microprocesador es algo lento")

    def Gamer(self):
        if self.AltaGama == False:
            print("El microprocesador no es recomendable para vieojuegos")
        else:
            print("El microprocesador es apto")

Intel = Procesador()
Intel.Nucleos=8
Intel.Generación
Intel.Marca="Intel"
Intel.Linea="Core"
Intel.Modelo=7
Intel.AltaGama

AMD = Procesador ()
AMD.Nucleos=6
AMD.Generación=8
AMD.Marca
AMD.Linea="A"
AMD.Modelo=3
AMD.AltaGama = False