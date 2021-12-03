#la diferencia entre estas dos variables "__dict__":
# la de la clase y la del objeto.
#
class ClaseEjemplo:
    varia = 1
    def __init__(self, val):
        ClaseEjemplo.varia = val
        self.__varia = val

print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)