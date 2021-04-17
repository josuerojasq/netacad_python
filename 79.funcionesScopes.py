#Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.
def miFuncion():
    print("¿Conozco a la variable?", var)

var = 1
miFuncion()
print(var)

#Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre.
def miFuncion2():
    var2 = 2
    print("¿Conozco a la variable?", var2)

var2 = 1
miFuncion2()
print(var2)

#La palabra reservada llamada "global" puede extender el alcance de una variable
#incluyendo el cuerpo de las funciones para poder no solo leer los valores de las variables
#sino también modificarlos.
def miFuncion3():
    global var3
    var3 = 2
    print("¿Conozco a aquella variable?", var3)

var3 = 1
miFuncion3()
print(var3)

#Al cambiar el valor del parámetro este no se propaga fuera de la función
#Esto también significa que una función recibe el valor del argumento,
#no el argumento en sí.
def miFuncion4(n):
    print("Yo obtuve", n)
    n += 1
    print("Yo ahora tengo", n)

varn = 1
miFuncion4(varn)
print(varn)

def miFuncionl(miLista1):
    print(miLista1)
    miLista1 = [0, 1]

miLista2 = [2, 3]
miFuncionl(miLista2)
print(miLista2)

def miFuncionl2(miLista1):
    print(miLista1)
    del miLista1[0]

miLista2 = [2, 3]
miFuncionl2(miLista2)
print(miLista2)
