#Las cadenas en Python pueden ser comparadas usando el mismo conjunto de operadores
# que se emplean con los números.
#Existe un "pero": los resultados de tales comparaciones a veces pueden ser un poco sorprendentes.
# Python no es consciente de problemas lingüísticos sutiles,
# simplemente "compara valores de puntos de código", caracter por caracter.
print('alfa' == 'alfa')
print('alfa' != 'Alfa')
print()

#Cuando se comparan dos cadenas de diferentes longitudes
# y la más corta es idéntica a la más larga, la cadena más larga se considera mayor.
print('alfa' < 'alfabeto')
print()

#La comparación de cadenas siempre distingue entre mayúsculas y minúsculas
# (las letras mayúsculas se consideran menores en comparación con las minúsculas).
print('beta' > 'Beta')
print()

#Aún si una cadena contiene solo dígitos, todavía no es un número.
# Se interpreta como lo que es, como cualquier otra cadena regular,
# y su aspecto numérico (potencial) no se toma en cuenta, en ninguna manera.
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')
print()

#Comparar cadenas contra números generalmente es una mala idea.
#Las únicas comparaciones que puede realizar con impunidad
# son aquellas simbolizadas por los operadores "==" y "!=".
# El primero siempre devuelve "False", mientras que el segundo siempre devuelve "True".
#El uso de cualquiera de los operadores de comparación restantes generará una excepción "TypeError".
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
#print('10' > 10) Esta expresion genera una excepcion de tipo "TypeError"
print()

