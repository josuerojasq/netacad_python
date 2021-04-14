#Escribir un programa que elimine todas las repeticiones de números de la lista.
#El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
#miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# coloca tu código aquí
#
miLista = []
listaTemp = []
num = int (input("¿Cuántos elementos deseas ingresar?:"))

for i in range(num):
    val = int(input("Introduce un elemento de la lista:"))
    miLista.append(val)

for elemento in miLista:
    if elemento not in listaTemp:
        listaTemp.append(elemento)

miLista = listaTemp[:]
print("La lista solo con elementos únicos:")
print(miLista)