#Si conoces el punto de código (número) y deseas obtener el carácter correspondiente,
# puedes usar la función llamada "chr()".
#La función toma un punto de código y devuelve su carácter.
#Invocándolo con un argumento inválido (por ejemplo, un punto de código negativo o inválido)
# provoca las excepciones "ValueError" o "TypeError".

print(chr(97))
print(chr(945))
print(chr(83))
print()

#Nota:
#chr(ord(x)) == x
#ord(chr(x)) == x

letra = 'a'
codigo = 97

print(chr(ord(letra)) == letra)
print(ord(chr(codigo)) == codigo)