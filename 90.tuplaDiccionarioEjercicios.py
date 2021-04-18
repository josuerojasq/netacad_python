#Ejercicio 1
miTup = (1, 2, 3)
print(miTup[2])
print()

#Ejercicio 2
tup = 1, 2, 3
a, b, c = tup

print(a * b * c)
print()

#Ejercicio 3
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicados = tup.count(2)

print(duplicados)    # salida: 4
print()

#Ejercicio 4
#Programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for elemento in (d1, d2):
    #print(elemento) Verificando la variable elemento
    #print(type(elemento)) Verificando la variable elemento
    d3.update(elemento)

print(d3)
print()

#Ejercicio 5
#Programa que convierta la lista l en una tupla.
l = ["carro", "Ford", "flor", "Tulipán"]
t = tuple(l)

print(t)
print()

#Ejercicio 6
#Programa que convierta la tupla colores en un diccionario.
colores = (("verde", "#008000"), ("azul", "#0000FF"))

colDict = dict(colores)

print(colDict)
print()

#Ejercicio 7
myDict = {"A":1, "B":2}
copyMiDict = myDict.copy()
myDict.clear()

print(copyMiDict)
print(myDict)
print()

#Ejercicio 8
colores = {
    "blanco" : (255, 255, 255),
    "gris"   : (128, 128, 128),
    "rojo"   : (255, 0, 0),
    "verde"  : (0, 128, 0)
    }

for col, rgb in colores.items():
    #print(type(col))
    #print(type(rgb))
    print(col, ":", rgb)