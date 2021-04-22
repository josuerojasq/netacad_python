#Si una excepción se genera dentro de una función, puede ser manejada:
#Dentro de la función.
#Fuera de la función.
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

x = int(input("Ingresa un numero: "))
print("1 /",x,"=",badFun(x))

print("FIN.")