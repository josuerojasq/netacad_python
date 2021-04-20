#Importar un modulo de la biblioteca de Python
import math

#como pueden dos namespaces (el tuyo y el del módulo) coexistir.
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14
print(sin(pi/2))

#Acceder a los nombres del modulo math (namespace)
print(math.sin(math.pi/2))

