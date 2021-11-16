#Imprimir la palabra con mayor letras

X = input("Escribir primer palabra: ")
First = (X)
Y = input("Escribir segunda palabra: ")
Second = (Y)

if len(First) > len(Second):
	print(First)
elif len(First) < len(Second):
	print(Second)
else: 
	print("Error")

print("Finalizado")