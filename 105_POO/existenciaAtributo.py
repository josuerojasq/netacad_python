#Es posible que no esperes que todos los objetos de la misma clase tengan
# los mismos conjuntos de propiedades.
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
#Esto genera un error de tipo "AttributeError"
#print(objetoEjemplo.b)

#Puedes evitar el problema con (no se recomienda):
try:
    print(objetoEjemplo.b)
except AttributeError:
    pass