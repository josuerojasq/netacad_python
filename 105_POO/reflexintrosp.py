#"getattr()" toma dos argumentos: un objeto y su nombre de propiedad (como una cadena)
# y devuelve el valor del atributo actual.
#La función "isinstance()" - comprueba si el valor es de tipo entero
#La función "setattr()"; toma tres argumentos: un objeto, el nombre de la propiedad (como una cadena)
# y el nuevo valor de la propiedad.
class MiClase:
    pass

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)