numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

#Un nuevo elemento puede ser añadido al final de la lista existente:
#Dicha operación se realiza mediante un método llamado "append()".
#Toma el valor de su argumento y lo coloca al final de la lista que posee el método.
#La longitud de la lista aumenta en uno.

numeros.append(4)

print(len(numeros))
print(numeros)

#El método "insert()" es un poco más inteligente:
#puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.
# - lista.insert(ubicación,valor)
#Nota: todos los elementos existentes que ocupan ubicaciones a la derecha del nuevo elemento
#(incluido el que está en la posición indicada) se desplazan a la derecha,
#para hacer espacio para el nuevo elemento.

numeros.insert(0,222)
print(len(numeros))
print(numeros)

numeros.insert(3,777)
print(len(numeros))
print(numeros)

#Extra:
#Python ofrece una forma más conveniente de hacer el intercambio de variables, echa un vistazo:
#Metodo tradicional
variable1 = 1
variable2 = 2

auxiliar = variable1
variable1 = variable2
variable2 = auxiliar

print(variable1, variable2)

#forma de intercambio en Python
variable1, variable2 = variable2, variable1

print(variable1, variable2)