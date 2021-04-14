#Escribe un programa que refleje estos cambios y te permita practicar con el concepto de listas.
#Tu tarea es:

#Paso 1: Crea una lista vacía llamada beatles.
#Paso 2: Emplea el método "append()" para agregar los siguientes miembros de la banda a la lista:
#John Lennon, Paul McCartney y George Harrison.
#Paso 3: Emplea el ciclo "for" y el "append()" para pedirle al usuario que agregue los siguientes miembros
#de la banda a la lista: Stu Sutcliffe, y Pete Best.
#Paso 4: Usa la instrucción "del" para eliminar a Stu Sutcliffe y Pete Best de la lista.
#Paso 5: Usa el método "insert()" para agregar a Ringo Starr al principio de la lista.

# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    if i == 0:
        beatles.append(input("Por favor agrega a Stu Sutcliffe a la lista de los Beatles: \n"))
    else:
        beatles.append(input("Por favor agrega a Pete Best a la lista de los Beatles: \n"))
print("Paso 3:", beatles)

# etapa 4
del beatles[4]
del beatles[3]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))