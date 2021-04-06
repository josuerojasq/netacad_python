#Desde la introducción del calendario gregoriano (en 1582),
#se utiliza la siguiente regla para determinar el tipo de año:
# Si el número del año no es divisible entre cuatro, es un año común.
# De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# De lo contrario, si el número del año no es divisible entre 400, es un año común.
# De lo contrario, es un año bisiesto.

anio = int(input("Introduzca un año:"))

#
# Coloca tu código aquí.
#
if anio >= 1582:
    if (anio % 4) != 0 : print("Año comun")
    elif (anio % 100) != 100 : print("Año bisiesto")
    elif (anio % 400) != 400 : print("Año comun")
    else: print("Año bisiesto")
else: print("No dentro del período del calendario gregoriano")