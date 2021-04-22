#Para saber el valor del punto de código ASCII/UNICODE de un caracter específico,
# puedes usar la función "ord()" (proveniente de ordinal).
#La función necesita una cadena de un caracter como argumento
# - incumplir este requisito provoca una excepción TypeError,
# y devuelve un número que representa el punto de código del argumento.
ch1 = 'a' 
ch2 = ' ' # espacio

print(ord(ch1))
print(ord(ch2))
print()

ch3 = 'α'
ch4 = 'ę'

print(ord(ch3))
print(ord(ch4))