#"__bases__" es una tupla, contiene clases (no nombres de clases)
# que son superclases directas para la clase.
#Nota: solo las clases tienen este atributo - los objetos no.
#Nota: una clase sin superclases explícitas apunta al objeto
# (una clase de Python predefinida) como su antecesor directo
class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)