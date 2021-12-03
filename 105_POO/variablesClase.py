#Una variable de clase es una propiedad que existe en una sola copia y se almacena fuera de cualquier objeto.
#Las variables de clase no se muestran en el diccionario de un objeto
#Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).
class ClaseEjemplo:
    contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)