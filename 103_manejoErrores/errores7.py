#La instrucción "raise" genera la excepción especificada denominada "exc"
# como si fuese generada de manera natural. Permite:
#Simular excepciones reales (por ejemplo, para probar tu estrategia de manejo de excepciones).
#Parcialmente manejar una excepción y hacer que otra parte del código sea responsable
# de completar el manejo.
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")