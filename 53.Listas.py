#Una "lista" es una colección de elementos
#Los elementos dentro de una "lista" pueden tener diferentes tipos.
#Los elementos de una "lista" están siempre numerados desde cero.

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprime el contenido de la lista original

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.

print("\nAccediendo al primer elemento de la lista:", numeros[0]) # accediendo al primer elemento de la lista. 

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

#Cualquier elemento de la lista puede ser eliminado en cualquier momento,
#esto se hace con una instrucción llamada "del" (eliminar).
# Nota: es una instrucción, no una función.
#No puedes acceder a un elemento que no existe, no puedes obtener su valor ni asignarle un valor.
del numeros[1] # eliminando el segundo elemento de la lista
print("\nLongitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

#Puede parecer extraño, pero los índices negativos son válidos y pueden ser muy útiles.
#Un elemento con un índice igual a -1 es el último en la lista.
print("\n Ultimo de la lista: ", numeros[-1])
print("\n Primero de la lista: ", numeros[-4])