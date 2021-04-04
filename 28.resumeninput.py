#La función print() envía datos a la consola, mientras que la función input() obtiene datos de la consola.

nombre = input("Ingresa tu nombre: ")
print("Hola, " + nombre + ". ¡Un gusto conocerte!")

num1 = input("Ingresa el primer número: ") # Ingresa 12
num2 = input("Ingresa el segundo número: ") # Ingresa 21
print(num1 + num2) # el programa regresa 1221

miEntrada = input("Ingresa Algo: ") # Ejemplo: hola
print(miEntrada * 3) # Salida esperada: holaholahola

#Replica el string "5" el numero de veces que ingresamos
x = int(input("Ingresa un número: ")) #  el usuario ingresa un 2
print(x * "5")

x = input("Ingresa un número: ") # el usuario ingresa un 2
print(type(x))

print("\nPresiona la tecla Enter para finalizar el programa.")
input()
print("FIN.")