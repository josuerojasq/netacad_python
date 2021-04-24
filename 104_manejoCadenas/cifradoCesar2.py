#escribir un programa el cual:
#Le pida al usuario una línea de texto para encriptar.
#Le pida al usuario un valor de cambio
# (un número entero del rango 1 al 25, nota: debes obligar al usuario a ingresar un valor de cambio válido
# (¡no te rindas y no dejes que los datos incorrectos te engañen!).
#Imprime el texto codificado.
#Dejemos que el código conserve las mayúsculas y minúsculas (las minúsculas permanecerán en minúsculas)
# y todos los caracteres no alfabéticos deben permanecer intactos.
def cifradoCesar(text, displace):
    cifrado = ""
    for char in text:
        if not char.isalpha(): cifrado += char
        else:
            code = ord(char) + displace
            if ord(char) <= ord('Z'):
                if code > ord('Z'): code = ord('A') + (code - ord('Z')) - 1
            else:
                if code > ord('z'): code = ord('a') + (code - ord('z')) - 1
            cifrado += chr(code)
    return cifrado


try:
    text = input("Ingresa tu mensaje a ser cifrado: ")
    sw = True
    while sw:
        displace = int(input("Ingresa el valor de cambio del cifrado 1 - 25: "))
        if not (displace > 0 and displace < 26):
            print("Debes ingresar un valor entre 1 y 25...")
            continue
        else:
            print(cifradoCesar(text, displace))
            sw = False
except ValueError:
    print("Has ingresado un valor que no es un numero entero!!!")