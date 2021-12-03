class ClaseEjemplo:
    def __init__(self, val = 1):
        self.primera = val

    def setSegunda(self, val):
        self.segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.tercera = 5

#Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto de propiedades y métodos
# predefinidos. Cada objeto los tiene, los quieras o no. Uno de ellos es una variable llamada "__dict__"
# (es un diccionario). La variable contiene los nombres y valores de todas las propiedades (variables)
# que el objeto contiene actualmente
print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)