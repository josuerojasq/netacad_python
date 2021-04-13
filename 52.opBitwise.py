#Hay cuatro operadores que le permiten manipular bits de datos individuales.
#Se denominan operadores "bitwise".
#Aquí están todos ellos:
# &  (ampersand) - conjunción a nivel de bits.
# |  (barra vertical) - disyunción a nivel de bits.
# ~  (tilde) - negación a nivel de bits.
# ^  (signo de intercalación) - exclusivo a nivel de bits o (xor).
#Agreguemos un comentario importante: los argumentos de estos operadores deben ser enteros.
#No debemos usar flotantes aquí.
i = 15
j = 22

log = bool(i and j)

bit = i & j

print(log)
print(bit)

logneg = bool(not i)
bitneg = ~i

print(logneg)
print(bitneg)

flagRegister = 1000
theMask = 8
if flagRegister & theMask:
    print("mi bit está listo")
else:
    print("mi bit se restablece")
print(flagRegister & theMask)

#Python ofrece otra operación relacionada con los bits individuales: shifting.
#Esto se aplica solo a los valores de número entero, y no debe usar flotantes como argumentos para ello.
#Los operadores de cambio en Python son un par de dígrafos: "<<" y ">>",
#sugiriendo claramente en qué dirección actuará el cambio.
var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)

#17 // 2 → 8 (desplazarse hacia la derecha en un bit equivale a la división de enteros en dos)
#17 * 4 → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro).

x = 4
y = 1

a = x & y
b = x | y
c = ~ x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f) 