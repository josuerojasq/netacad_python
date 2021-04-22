#las cadenas pueden ser:
#Concatenadas (unidas).
#El operador "+" es empleado en dos o más cadenas y produce una nueva cadena que
# contiene todos los caracteres de sus argumentos
# (nota: el orden es relevante aquí, en contraste con su versión numérica, la cual es conmutativa).
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print()

#Replicadas.
#El operador "*" necesita una cadena y un número como argumentos; en este caso, el orden no importa:
# puedes poner el número antes de la cadena, o viceversa, el resultado será el mismo:
# una nueva cadena creada por la enésima replicación de la cadena del argumento.
print(5 * str1)
print(str2 * 4)
print()

#Los atajos de los operadores anteriores también son aplicables para las cadenas (+= y *=).
str2 += str1
str1 *= 5

print(str2)
print(str1)