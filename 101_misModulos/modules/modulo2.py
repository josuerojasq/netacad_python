#! /bin/python3
""" modulo2.py - un ejemplo de modulos en Python """

_counter = 0

def suma(list):
    global _counter
    _counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def producto(list):
    global _counter
    _counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("Prefiero ser un módulo, pero puedo hacer una prueba por ti.")
    l = [i+1 for i in range(5)]
    print(suma(l) == 15)
    print(producto(l) == 120)