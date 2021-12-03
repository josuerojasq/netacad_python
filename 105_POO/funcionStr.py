#forma en que el objeto puede presentarse a si mismo.
class Estrella0:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

sol0 = Estrella0("Sol", "Vía Láctea")
#Genera <__main__.Estrella0 object at 0x7f377e552160> algo asi
print(sol0)
print()

#El método por default "__str__()" devuelve la cadena anterior: fea y poco informativa.
# Puedes cambiarlo definiendo tu propio método del nombre.
class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)