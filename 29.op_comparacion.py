#"=" es un operador de asignación, por ejemplo, a = b asigna a la varable a el valor de b.
#"==" es una pregunta ¿Son estos valores iguales?; a == b compara a y b.
var = 0 # asignando 0 a var
print(var == 0)

var = 1 # asignando 1 a var
print(var == 0)

#El operador "!=" (no es igual a) también compara los valores de dos operandos.
# Aquí está la diferencia: si son iguales, el resultado de la comparación es "False".
# Si no son iguales, el resultado de la comparación es "True".
var = 0 # asignando 0 a var
print(var != 0)

var = 1 # asignando 1 a var
print(var != 0)

#Usando el operador ">" (mayor que)
ovejasNegras = 15
ovejasBlancas = 22
print("Hay mas ovejas Negras que Blancas?")
print(ovejasNegras > ovejasBlancas)

#Una variante no estricta, ">=" (mayor o igual que).
centigradosAfuera = -2.0
print("No tenemos que usar gorrito hoy?")
print(centigradosAfuera >= 0.0)

#El operador "<" (menor que) y su hermano no estricto: "<=" (menor o igual que).
velocidadMph = 85
print(velocidadMph < 85) # menor que.
print(velocidadMph <= 85) # menor o igual que.