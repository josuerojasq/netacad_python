#Tu programa debe:
#Pedir al usuario que ingrese una palabra.
#Utiliza userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas;
#Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales
#A , E , I , O , U de la palabra ingresada.
#Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)

#Asigne las letras no consumidas a la variable "palabrasinVocal" e imprime la variable en la pantalla.
palabraSinVocal = ""
userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabraSinVocal += letra
print(palabraSinVocal)