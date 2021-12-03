#Si se nombra un método de esta manera: "__init__", no será un método regular, será un constructor.
#Si una clase tiene un constructor, este se invoca automática e implícitamente
# cuando se instancia el objeto de la clase.
#El constructor:
#Esta obligado a tener el parámetro "self" (se configura automáticamente).
#Pudiera (pero no necesariamente) tener mas parámetros que solo "self"; si esto sucede,
# la forma en que se usa el nombre de la clase para crear el objeto debe tener la definición "__init__".
#Se puede utilizar para configurar el objeto, es decir, inicializa adecuadamente su estado interno,
# crea variables de instancia, crea instancias de cualquier otro objeto si es necesario, etc.
#No puede retornar un valor, ya que está diseñado para devolver un objeto recién creado y nada más.
#No se puede invocar directamente desde el objeto o desde dentro de la clase
class conClase:
    def __init__(self, valor):
        self.var = valor

obj1 = conClase("objeto")

print(obj1.var)
print()

#Como "__init__" es un método, y un método es una función,
# puedes hacer los mismos trucos con constructores y métodos que con las funciones ordinarias.
#Definir un constructor con un valor de argumento predeterminado:
class conClase2:
    def __init__(self, valor = None):
        self.var = valor

obj2 = conClase2("objeto")
obj3 = conClase2()

print(obj2.var)
print(obj3.var)
print()