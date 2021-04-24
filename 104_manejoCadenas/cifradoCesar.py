#Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César y sus tropas
# durante las Guerras Galas. La idea es bastante simple:
# cada letra del mensaje se reemplaza por su consecuente más cercano
# (A se convierte en B, B se convierte en C, y así sucesivamente).
# La única excepción es Z, la cual se convierte en A.

text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)

#La operación inversa
# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)