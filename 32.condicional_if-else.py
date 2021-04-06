#Condicional "if - else"

#Condicional "if"

centigradosAfuera = float(input("Cuantos grados centigrados tenemos afuera?\n"))

if centigradosAfuera >= 20.0:  #evalúa una expresión de prueba.
    print("Vamonos de caminata...") #se ejecuta si la expresión de prueba es Verdadera.
else:
    print("Vamos al cine...") #se ejecuta si la expresión de prueba es Falsa.
print("Al final de todo almorzaremos") #no pertenece al bloque "if - else", lo que significa que siempre se ejecuta.

#lee dos números
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado
print("El número más grande es:", nmasGrande)

#Lo mismo pero mas corto //
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))

# elegir el número más grande
if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

#imprimir el resultado
print("El número más grande es: ", nmasGrande)

#lee tres números
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))
numero3 = int (input("Ingresa el tercer número: "))

#asumimos temporalmente que el primer número
#es el más grande
#lo verificaremos pronto
nmasGrande = numero1

#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3

#imprimir el resultado
print("El número más grande es:", nmasGrande)