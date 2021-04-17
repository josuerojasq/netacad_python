#La instrucción "return" tiene dos variantes diferentes: considerémoslas por separado.

#return sin una expresión
#La primera consiste en la palabra reservada en sí, sin nada que la siga.
#Cuando se emplea dentro de una función, provoca la terminación inmediata de la ejecución de la función,
#y un retorno instantáneo (de ahí el nombre) al punto de invocación.
def felizAnioNuevo(deseos = True):
    print("Tres ...")
    print("Dos ...")
    print("Uno ...")
    if not deseos:
        return
    print("¡Feliz año nuevo!")

felizAnioNuevo()
felizAnioNuevo(False)

#return con una expresión
#La segunda variante de return está extendida con una expresión:
def funcion_aburrida():
    return 123

x = funcion_aburrida()

print ("La funcion_aburrida ha devuelto su resultado. Es: ", x)