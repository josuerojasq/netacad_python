#La propiedad "__name__" contiene el nombre de la clase. Es solo una cadena.
#Nota: el atributo "__name__" está ausente del objeto - existe solo dentro de las clases.
#Si deseas encontrar la clase de un objeto en particular, puedes usar una función llamada "type()",
# la cual es capaz (entre otras cosas) de encontrar una clase que se haya utilizado
# para crear instancias de cualquier objeto.
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)