#¡El orden de las excepciones importa!
#No pongas excepciones más generales antes que otras más concretas.
#Esto hará que el último sea inalcanzable e inútil.
#Además, hará que el código sea desordenado e inconsistente.
#Python no generará ningún mensaje de error con respecto a este problema.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print("1 /",x,"=",y)
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema aritmético!")

print("FIN.")