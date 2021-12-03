#Define la clase Pila
class Pila:
    #Define la funcion del constructor...
    #El nombre del constructor es siempre "__init__"
    def __init__(self):
        #Agregando una propiedad a la clase Pila
        #Cuando el nombre de la propiedad comienza con dos guiones bajos (__), se vuelve privado
        self.__listaPila = [] #Encapsulacion
    
    #Funciones: Tal componente es llamado "publico", por ello no puede comenzar su nombre con dos
    # (o más) guiones bajos. Hay un requisito más - el nombre no debe tener más de un guión bajo.
    def push(self, val):
        self.__listaPila.append(val)
    
    #Todos los métodos deben tener este parámetro "self". Desde el constructor
    # Permite que el método acceda a entidades (propiedades y actividades / métodos) del objeto.
    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val

#Define una nueva subclase que apunte a la clase que se usará como superclase.
class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0
    
    #Cambiar la funcionalidad de los métodos, no sus nombres.
    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val
    
    def getSuma(self):
        return self.__sum

#Instanciando el objeto Pila
objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())

objPila = SumarPila()

for i in range(5):
    objPila.push(i)
print(objPila.getSuma())

for i in range(5):
    print(objPila.pop())
