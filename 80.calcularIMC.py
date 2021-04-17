#La función hace lo que deseamos, pero es un poco sencilla
#Asume que los valores de ambos parámetros son significativos.
#Se debe comprobar que son confiables.
#el símbolo de "diagonal invertida (\)" es empleado.
#Si se termina una línea de código con el,
#Python entenderá que la línea continua en la siguiente.
def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    return peso / altura ** 2

#convertir unidades del sistema inglés al sistema métrico
def lbakg(lb):
    return lb * 0.45359237

def piepulgam(pie, pulgada = 0.0):
    return pie * 0.3048 + pulgada * 0.0254


print(piepulgam(1, 1))
print(lbakg(1))
print(imc(52.5, 1.65))
print(imc(peso = lbakg(176), altura = piepulgam(5, 7)))