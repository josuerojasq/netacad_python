#Se produce una excepción concreta cuando falla una operación de importación.
# una de estas importaciones fallará, ¿cuál será?

try:
    import math
    import time
    import abracadabra

except:
    print('Una de sus importaciones ha fallado.')