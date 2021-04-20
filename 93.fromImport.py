#Señala con precisión qué entidad (o entidades) del módulo son aceptables en el código
#lleva a cabo la importación selectiva.
from math import sin, pi

#Hace uso de las entidades importadas y obtiene el resultado esperado (1.0).
print(sin(pi/2))

#Redefine el significado de "pi" y "sin" - en efecto,
#Reemplazan las definiciones originales (importadas) dentro del namespace del código.
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

#retorna 0.99999999, lo cual confirma nuestras conclusiones.
print(sin(pi/2))