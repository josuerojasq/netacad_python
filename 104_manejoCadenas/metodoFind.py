#El método "find()" es similar al método index() - busca una subcadena
# y devuelve el índice de la primera aparición de esta subcadena, pero:
#Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente
# (devuelve -1 en dicho caso).
#Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.
print("Eta".find("ta"))
print("Eta".find("mma"))
print()

t = 'teta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('te'))
print(t.find('ha'))
print()

#Si deseas realizar la búsqueda, no desde el principio de la cadena, sino desde cualquier posición,
# puedes usar una variante de dos parámetros del método "find()"
print('kappa'.find('a', 2))
print()

#Se puede emplear el método find() para buscar todas las ocurrencias de la subcadena
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)
print()

#Mutación de tres parámetros del método "find()"
# El tercer argumento apunta al primer índice que no se tendrá en cuenta durante la búsqueda
# (en realidad es el límite superior de la búsqueda).
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))