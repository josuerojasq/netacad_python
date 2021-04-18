#Importar un modulo de la biblioteca de Python
import math

#Acceder a los nombres del modulo math (namespace)
print(math.sin(math.pi/2))

coordDict = {
    1:(0, 0), 2:(0, 1), 3:(0, 2),
    4:(1, 0), 5:(1, 1), 6:(1, 2),
    7:(2, 0), 8:(2, 1), 9:(2, 2),
    }
print(coordDict[8])