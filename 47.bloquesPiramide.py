#Escribir un programa que lea la cantidad de bloques que tienen los constructores,
#y generar la altura de la pirámide que se puede construir utilizando estos bloques.
#Nota: La altura se mide por el número de capas completas:
#si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa,
#terminan su trabajo inmediatamente.
bloques = int(input("Ingrese el número de bloques: "))
altura = 0
bloquesxPiso = 0
bloquesUsados = 0

while True:
    bloquesxPiso += 1
    bloquesUsados += bloquesxPiso
    if bloquesUsados <= bloques:
        altura += 1
    else:
        break
print("La altura de la pirámide:", altura)