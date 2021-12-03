#Un método es una función que está dentro de una clase.
#Requisito fundamental: un método está obligado a tener al menos un parámetro
#El primer (o único) parámetro generalmente se denomina "self"
#"self" - identifica el objeto para el cual se invoca el método.
#Si vas a invocar un método, no debes pasar el argumento para el parámetro "self"
# Python lo configurará por ti.
class conClase:
    def metodo(self):
        print("Método sin parametros!")

obj = conClase()
obj.metodo()
print()

#Si deseas que el método acepte parámetros distintos a "self", debes:
#Colocarlos después de "self" en la definición del método.
#Pasarlos como argumentos durante la invocación sin especificar "self".
class conClase2:
    def metodo2(self, par):
        print("Método con parametros:", par)

obj2 = conClase2()
obj2.metodo2(1)
obj2.metodo2(2)
obj2.metodo2(3)
print()

#El parámetro "self" es usado para obtener acceso a la instancia del objeto y las variables de clase.
class conClase3:
    varia = 2
    def metodo3(self):
        print(self.varia, self.var)

obj3 = conClase3()
obj3.var = 3
obj3.metodo3()
print()

#El parámetro "self" también se usa para invocar otros métodos desde dentro de la clase.
class conClase4():
    def otro(self):
        print("otro")

    def metodo4(self):
        print("método")
        self.otro()

obj4 = conClase4()
obj4.metodo4()
print()

#Un método cuyo nombre comienza con "__" está (parcialmente) oculto.
class conClase5:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj5 = conClase5()
obj5.visible()

try:
    obj5.__oculto()
except:
    print("fallido")

obj5._conClase5__oculto()