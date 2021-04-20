#La función general llamada "random()" produce un número flotante x entre el rango (0.0, 1.0)
#en otras palabras: (0.0 <= x < 1.0).
#La función "seed()" es capaz de establecer la semilla del generador:
#seed() - establece la semilla con la hora actual.
#seed(int_value) - establece la semilla con el valor entero "int_value".
from random import random, seed

for i in range(5):
    print(random())
print()

seed(0)
for i in range(5):
    print(random())
print()

#valores aleatorios enteros, una de las siguientes funciones encajaría mejor:
#randrange(fin)
#randrange(inico, fin)
#randrange(inicio, fin, incremento)
#randint(izquierda, derecha)
#Las primeras tres invocaciones generarán un número entero tomado (pseudoaleatoriamente) del rango:
#range(fin)
#range(inicio, fin)
#range(inicio, fin, incremento)
#Toma en cuenta la exclusión implícita del lado derecho.
#La última función es equivalente a "randrange(izquierda, derecha+1)"
# genera el valor entero i, el cual cae en el rango [izquierda, derecha]
# (sin exclusión en el lado derecho).
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
print()

#Es muy probable que el programa genere un conjunto de números en el que algunos elementos no sean únicos
for i in range(10):
    print(randint(1, 10), end=',')
print("\n")

#Es una función con el nombre de - choice:
#"choice(secuencia)"
#"sample(secuencia, elementos_a_elegir=1)"
#La primera variante elige un elemento "aleatorio" de la secuencia de entrada y lo devuelve.
#El segundo crea una lista (una muestra) que consta del elemento "elementos_a_elegir"
#(que por defecto es 1) "sorteado" de la secuencia de entrada.
from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))