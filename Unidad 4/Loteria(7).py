#Sorteo del 1 al 10 
## Alexis David Zambrano Ibarra

num = int(input("Ingresar un numero del 1 al 10; "))
import random
M = random.randint(1,10)

if num == M:
	print(num, "Felicidades ganaste")
else:
	print(num, "Perdiste, suerte para la proxima")

print("Finalizado")