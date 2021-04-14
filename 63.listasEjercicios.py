#Intenta encontrar el mayor valor en la lista.
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista[0]

for i in range(1, len(miLista)):
   if miLista [i]> mayor:
        mayor = miLista[i]

print(mayor)

#encontremos la ubicación de un elemento dado dentro de una lista:
miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 6
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

#Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.
#Los números que han salido sorteados son: 5, 11, 9, 42, 3, 49.
#La pregunta es: ¿A cuántos números le has atinado?
sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)#La salida del programa es: 4.