#Un diccionario es un conjunto de pares de claves y valores.#
# -Cada clave debe de ser única. No es posible tener una clave duplicada.
# -Una clave puede ser un tipo de dato de cualquier tipo:
# puede ser un número (entero o flotante), o incluso una cadena.
# -Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados,
# mientras que un diccionario almacena pares de valores.
# -La función "len()" aplica también para los diccionarios,
# regresa la cantidad de pares (clave-valor) en el diccionario.
# -Un diccionario es una herramienta de un solo sentido.
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'boss' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)
print(dict['gato'])
print(numerosTelefono['Suzy'])
print()

words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")
print()

#¿Pueden los diccionarios ser examinados utilizando el bucle "for", como las listas o tuplas?
#No y si.
# -No, porque un diccionario no es un tipo de dato secuencial - el bucle "for" no es útil aquí.
# -Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario
#  a los requerimientos del bucle "for"(en otras palabras, se construye un enlace intermedio
#  entre el diccionario y una entidad secuencial temporal).
#Método "keys()", el cual es parte de todo diccionario.
# El método retorna o regresa una lista de todas las claves dentro del diccionario.
for key in dict.keys():
    print(key, "->", dict[key])
print()

#La función "sorted()" ordena la salida en el for del diccionario
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
print()

#El método "items()". Este método regresa una lista de tuplas
#donde cada tupla es un par de cada clave con su valor.
for spanish, french in dict.items():
    print(spanish, "->", french)
print()

#El método "values()", funciona de manera muy similar al de keys(),
#pero regresa una lista de valores.
for french in dict.values():
    print(french)
print()

#Asignar un nuevo valor a una clave existente es sencillo,
#debido a que los diccionarios son completamente mutables
dict['gato'] = 'minou'

#Agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor.
#Solo se tiene que asignar un valor a una nueva clave que no haya existido antes.
dict['cisne'] = 'cygne'

#También es posible insertar un elemento al diccionario utilizando el método "update()"
dict.update({"pato" : "canard"})
print(dict)
print()

#Al eliminar la clave también se removerá el valor asociado. Los valores no pueden existir sin sus claves.
#Esto se logra con la instrucción "del".
del dict['perro']

#Para eliminar el ultimo elemento de la lista, se puede emplear el método "popitem()"
dict.popitem()
print(dict)