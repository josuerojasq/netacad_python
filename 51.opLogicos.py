#Un operador de conjunción lógica en Python es la palabra "and".
#Es un operador binario con una prioridad inferior a la expresada por los operadores de comparación
contador = 5
valor = 100
print(str(contador) + " > 0 and " + str(valor) + " == 100")
print(contador > 0 and valor == 100)

#Un operador de disyunción es la palabra "or".
#Es un operador binario con una prioridad más baja que and
print(str(contador) + " == 0 or " + str(valor) + " < 100")
print(contador == 0 or valor < 100)

#"not" Es un operador unario que realiza una negación lógica.
#Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad.
print("not " + str(valor) + " == 100")
print(not valor == 100)

#Las siguientes condiciones son equivalentes a pares
var = 1
print(var > 0)
print(not (var <= 0))

print(var != 0)
print(not (var == 0))

#Ley de Morgan
p = True
q = False

print(not (p and q) == (not p) or (not q) )
print(not (p or q) == (not p) and (not q))