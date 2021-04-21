#La palabra reservada "try" comienza con un bloque de código el cual
# puede o no estar funcionando correctamente.
#Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción
# y Python comienza a buscar una solución.
try:
    print("1")
    x = 1 / 0 #Se divide entre 0 deliberadamente
    print("2")
#La palabra reservada "except" comienza con un bloque de código que será ejecutado
# si algo dentro del bloque "try" sale mal - si se genera una excepción dentro del bloque anterior "try",
# fallará aquí, entonces el código ubicado después de la palabra clave "except"
# debería proporcionar una reacción adecuada a la excepción planteada.
#Se regresa al nivel de anidación anterior, es decir, se termina la sección "try-except".
except:
    print("Oh cielos, algo salio mal...")

print("3")