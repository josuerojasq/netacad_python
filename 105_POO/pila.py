#La pila: el enfoque procedimental
#Primero, debes decidir cómo almacenar los valores que llegarán a la pila.
# Sugerimos utilizar el método más simple, y emplear una lista para esta tarea.
# Supongamos que el tamaño de la pila no está limitado de ninguna manera.
# Supongamos también que el último elemento de la lista almacena el elemento superior.
pila = []

#Función que pone un valor en la pila
def push(val):
    pila.append(val)

#Función que quite un valor de la pila
def pop():
    val = pila[-1]
    del pila[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())