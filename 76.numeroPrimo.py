#Escribir una función que verifique si un número es primo o no.
#Para saber si un número "es primo" basta con probar si el número no es divisible por los primos
#hasta su raiz cuadrada.
def isPrime(num):
    limite = int(round(num ** 0.5,0))
    esPrimo = True
    i = 2
    while esPrimo and i <= limite:
        if num % i == 0:
            esPrimo = False
        i += 1
    return esPrimo

for i in range(1, 100):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()