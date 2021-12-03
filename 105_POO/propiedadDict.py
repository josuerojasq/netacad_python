#Cada clase de Python y cada objeto de Python está pre-equipado con un conjunto de atributos útiles
# que pueden usarse para examinar sus capacidades.
#La propiedad "__dict__".
#Observemos cómo esta propiedad trata con los métodos.
#Encuentra todos los métodos y atributos definidos.
# Localiza el contexto en el que existen: dentro del objeto o dentro de la clase.
class conClase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)