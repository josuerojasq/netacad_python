#Si el "try" lanza la excepción "exc1", esta será manejada por el bloque "except exc1:".
#De la misma manera, si el "try" lanza la excepción "exc2", esta será manejada por el bloque "except exc2:".
#Si el "try" lanza cualquier otra excepción, será manejado por el bloque sin nombre "except".
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print("1 /",x,"=",y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")