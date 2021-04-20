#El módulo "platform" permite acceder a los datos de la plataforma subyacente, es decir,
#hardware, sistema operativo e información sobre la versión del intérprete.
#"platform(aliased = False, terse = False)"
#aliased → cuando se establece a True (o cualquier valor distinto de cero)
# puede hacer que la función presente los nombres de capa subyacentes alternativos en lugar de los comunes.
#terse → cuando se establece a True (o cualquier valor distinto de cero)
# puede convencer a la función de presentar una forma más breve del resultado (si lo fuera posible).
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))
print()

#A veces, es posible que solo se desee conocer el nombre genérico del procesador
# que ejecuta el sistema operativo junto con Python y el código,
# una función llamada "machine()" te lo dirá.
from platform import machine

print(machine())
print()

#La función "processor()" devuelve una cadena con el nombre real del procesador (si lo fuese posible).
from platform import processor

print(processor())
print()

#Una función llamada "system()" devuelve el nombre genérico del sistema operativo en una cadena.
from platform import system

print(system())
print()

#La versión del sistema operativo se proporciona como una cadena por la función "version()".
from platform import version

print(version())
print()

#Si necesitas saber qué versión de Python está ejecutando tu código, puedes verificarlo utilizando
# una serie de funciones dedicadas, aquí hay dos de ellas:
#"python_implementation()" → devuelve una cadena que denota la implementación de Python
# (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).
#"python_version_tuple()" → devuelve una tupla de tres elementos la cual contiene:
# -la parte mayor de la versión de Python.
# -la parte menor,
# -el número de nivel del patch.
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr,end=".")
print("\n")