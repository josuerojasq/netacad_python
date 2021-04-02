#Impresion de varios argumentos
#Una función print() invocada con más de un argumento genera la salida en una sola línea.
#La función print() pone un espacio entre los argumentos emitidos por iniciativa propia.
print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")
print()

#Argumentos de palabras clave
#Un argumento de palabra clave consta de tres elementos:
#   -Una palabra clave que identifica el argumento (end -termina aquí); 
#   -Un signo de igual (=);
#   -Y un valor asignado a ese argumento.
#Cualquier argumento de palabra clave debe ponerse después del último argumento posicional (esto es muy importante).
#"end" determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
print()

print("Mi nombre es", end="")
print("Monty Python.")
print()

#Cambiar el valor de separacion...
#El argumento de palabra clave que puede hacer esto se denomina "sep" (como separador).
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
print()

#Ambos argumentos de palabras clave pueden mezclarse en una invocación,
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="-\n")
print("Hola Mundo!!!")
print()

print("Fundamentos","Programación","en", sep="***", end="...")
print("Python")