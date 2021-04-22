#Si existe la posibilidad de que más de una excepción se salte a un apartado "except:",
# puedes tener problemas para descubrir lo que realmente sucedió.
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print("1 /",x,"=",y)
except:
#El mensaje: "Oh cielos, algo salio mal..." que aparece en la consola no dice nada acerca de la razón,
# mientras que hay dos posibles causas de la excepción:
#Datos no enteros fueron ingresados por el usuario.
#Un valor entero igual a 0 fue asignado a la variable x.
    print("Oh cielos, algo salio mal...")

print("FIN.")