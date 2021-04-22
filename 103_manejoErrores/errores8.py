#Esta variante de la instrucción "raise" puede ser utilizada solamente dentro de la rama "except";
# usarla en cualquier otro contexto causa un error.
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")