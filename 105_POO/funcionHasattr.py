#Función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica.
# La función se llama "hasattr", y espera que le pasen dos argumentos:
#La clase o el objeto que se verifica.
#El nombre de la propiedad cuya existencia se debe informar
# (Nota: debe ser una cadena que contenga el nombre del atributo).
#La función retorna True o False.
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)
print()

#La función "hasattr()" también puede operar en clases.
# Puedes usarlo para averiguar si una variable de clase está disponible
class ClaseEjemplo1:
    attr = 1

print(hasattr(ClaseEjemplo1, 'attr'))
print(hasattr(ClaseEjemplo1, 'prop'))
print()


class Ejemplo3:
    a = 1
    def __init__(self):
        self.b = 2

objetoEj3 = Ejemplo3()

print(hasattr(objetoEj3, 'b'))
print(hasattr(objetoEj3, 'a'))
print(hasattr(Ejemplo3, 'b'))
print(hasattr(Ejemplo3, 'a'))