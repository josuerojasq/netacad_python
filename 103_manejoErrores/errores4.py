#Cada excepción cae en la primer coincidencia.
#La coincidencia correspondiente no tiene que especificar exactamente la misma excepción,
# es suficiente que la excepción sea mas general (mas abstracta) que la lanzada.

#Si el "try" lanza la excepción "exc1", esta será manejada por el bloque "except exc1:".
#De la misma manera, si el "try" lanza la excepción "exc2", esta será manejada por el bloque "except exc2:".
#Si el "try" lanza cualquier otra excepción, será manejado por el bloque sin nombre "except".
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print("1 /",x,"=",y)
except ArithmeticError:
    print("No puedes dividir entre cero, lo siento.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")