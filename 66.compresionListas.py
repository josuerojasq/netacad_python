#Una comprensión de lista es en realidad una lista,
#pero se creó sobre la marcha durante la ejecución del programa,
#y no se describe de forma estática.

fila = []
PEON_BLANCO = "PEON_BLANCO"
for i in range(8):
    fila.append(PEON_BLANCO)
print(fila)
#Ejemplo 1
#Genera una lista de diez elementos y rellena con cuadrados de diez números enteros
#que comienzan desde cero
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)

#Ejemplo 2
#Arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos
#(1, 2, 4, 8, 16, 32, 64, 128)
dos = [2 ** i for i in range(8)]
print(dos)

#Ejemplo 3
#lista con solo los elementos impares de la lista cuadrados.
probabilidades = [x for x in cuadrados if x % 2 != 0] 
print(probabilidades)

#Ejemplo 4
#Tablero de ajedrez
#Los elementos de las filas son campos, ocho de ellos por fila.
#Los elementos del tablero de ajedrez son filas, ocho de ellos por tablero de ajedrez.
EMPTY = "EMPTY"
tablero = [[EMPTY for i in range(8)] for j in range(8)]
print(tablero)