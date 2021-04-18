#Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas.
# Cada diccionario es un par de clave : valor.
polEspDict = {
    "zamek" : "castillo",
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

#Acceder a un elemento del diccionario
#Haciendo referencia a su clave colocándola dentro de corchetes
elemento1 = polEspDict["gleba"]    # ejemplo 1
print(elemento1)    # salida: tierra

#Acceder a un elemento del diccionario
#Utilizando el método "get()"
elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua

#Cambiar el valor asociado a una clave especifica,
#haciendo referencia a la clave del elemento
polEspDict["zamek"] = "cerradura"
item = polEspDict["zamek"]    # salida: cerradura
print(item)
print()

#Agregar o eliminar una clave (junto con su valor asociado)
miDirectorioTelefonico = {}    # un diccionario vacio

miDirectorioTelefonico ["Adan"] = 3456783958    # crear o añadir un par clave-valor
print(miDirectorioTelefonico)    # salida: {'Adan': 3456783958}

del miDirectorioTelefonico ["Adan"]
print(miDirectorioTelefonico)    # salida: {}
print()

#Insertar un elemento a un diccionario utilizando el método "update()"
polEspDict.update({"powietrze" : "aire"})
print(polEspDict)

#Eliminar el ultimo elemento con el método "popitem()"
polEspDict.popitem()
print(polEspDict)
print()

#Emplear el bucle "for" para iterar a través del diccionario
for item in polEspDict:
    print(item)
print()

#Examinar los elementos (claves y valores) del diccionario, empleando el método "items()"
for clave, valor in polEspDict.items():
    print("Pol/Esp ->", clave, ":", valor)
print()

#Comprobar si una clave existe en un diccionario, emplear la palabra reservada "in"
if "zamek" in polEspDict:
    print("SI")
else:
    print("NO")
print()

#copiar un diccionario, con el método "copy()"
copyDict = polEspDict.copy()
print(copyDict)
print()

#Emplear la palabra reservada "del" para eliminar un elemento, o un diccionario entero.
print(len(polEspDict))    # salida: 4
del polEspDict["zamek"]    # elimina un elemento
print(len(polEspDict))    # salida: 3

#Para eliminar todos los elementos de un diccionario se debe emplear el método "clear()"
polEspDict.clear()   # elimina todos los elementos
print(len(polEspDict))    # salida: 0

del polEspDict    # elimina el diccionario