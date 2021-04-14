#Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos)
miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)

#calcular la suma de todos los valores almacenados en la lista
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma)

#La instrucción "for" especifica la variable utilizada para navegar por la lista (i)
#seguida de la palabra clave "in" y el nombre de la lista siendo procesado (miLista).
miLista = [20, 8, 2, 1, 2]
suma = 0

for i in miLista:
    suma += i

print(suma)

#Intercambiar fácilmente los elementos de la lista para revertir su orden
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista) 

longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista) 