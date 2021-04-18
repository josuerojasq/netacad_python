#Una tupla es una secuencia inmutable
#Los datos inmutables no pueden ser modificados libremente en cualquier momento
#Las tuplas utilizan paréntesis, aunque también es posible crear una tupla tan solo
#separando los valores por comas.
tupla1 = (1, 2, 4, 8)
tupla2 = 1., .5, .25, .125
tuplaVacia = ()
tuplaUnElemento1 = (1, )
tuplaUnElemento2 = 1., 

print(tupla1)
print(tupla2)

miTupla = (1, 10, 100, 1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)
print()

#La función "len()" acepta tuplas, y regresa el numero de elementos contenidos dentro.
#El operador "+" puede unir tuplas (ya se ha mostrado esto antes).
#El operador "*" puede multiplicar las tuplas, así como las listas.
#Los operadores "in" y "not in" funcionan de la misma manera que en las listas.
tupla3 = (1, 10, 100)

t1 = tupla3 + (1000, 10000)
t2 = tupla3 * 3

print(len(t2))
print(t1)
print(t2)
print(10 in tupla3)
print(-10 not in tupla3)