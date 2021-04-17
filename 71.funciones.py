#Una función es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada).
#Las funciones son útiles para hacer que el código sea reutilizable,
#que este mejor organizado y más legible.
#Las funciones contienen parámetros y pueden regresar valores.
#Así es como se ve la definición más simple de una función:
# def nombreFuncion(parámetros opcionales):
#     cuerpoFuncion
#Definimos la funcion "mensaje()"
def mensaje():
    print("Ingresa un valor:")

#Invocamos a la funcion "mensaje()"
mensaje()
a = int(input())

mensaje()
b = int(input())

mensaje()
c = int(input())

#Es posible definir funciones con argumentos:
def saludo(nombre):    # definiendo una función
    print("Hola,", nombre)    # cuerpo de la función

nombre = input("Ingresa tu nombre: ")

saludo(nombre)    # invocación de la función

#La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de "parámetros posicionales",
#los argumentos pasados de esta manera son llamados "argumentos posicionales".
def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")

presentar("Skywalker" ,"Luke" )
presentar("Quick", "Jesse")
presentar("Kent", "Clark")

#Otra manera de pasar argumentos, donde el significado del argumento esta definido por su nombre,
#no su posición, a esto se le denomina paso de argumentos con palabras clave.
presentar(primerNombre = "James", segundoNombre = "Bond")
presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

#El combinar argumentos posicionales y de palabras clave
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

suma(1, 2, 3)
suma(c = 1, a = 2, b = 3)
suma(3, c = 1, b = 2)

#En ocasiones ocurre que algunos valores de ciertos argumentos son mas utilizados que otros.
#Dichos argumentos tienen "valores predefinidos" los cuales pueden ser considerados
#cuando los argumentos correspondientes han sido omitidos.
def presentar2(primerNombre, segundoNombre="Smith"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar2("Jorge", "Pérez")
presentar2("Enrique")
presentar2(primerNombre="Guillermo")
