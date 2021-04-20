#! /bin/python3
""" miModulo.py - un ejemplo de modulos en Python """

_counter = 0

def sum1(list):
    global _counter
    _counter += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prod1(list):
    global _counter
    _counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("Prefiero ser un módulo, pero puedo hacer una prueba por ti.")
    l = [i+1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)