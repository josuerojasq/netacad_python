#Agregando dos guiones bajos (__) en frente de las propiedades.
#Como sabes, tal adición hace que la variable de instancia sea "privada"
# se vuelve inaccesible desde el mundo exterior.
class ClaseEjemplo:
    def __init__(self, val = 1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)

print(objetoEjemplo1._ClaseEjemplo__primera)