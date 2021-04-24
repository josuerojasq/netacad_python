#Escribir un programa que:
#Le pida al usuario algún texto.
#Compruebe si el texto introducido es un palíndromo e imprima el resultado.
#Nota:
#Supón que una cadena vacía no es un palíndromo.
#Trata las letras mayúsculas y minúsculas como iguales.
#Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
#Existe más de una solución correcta: intenta encontrar más de una.

texto = input("Ingresa el texto para saber si es palindromo: \n")
listaTxt = texto.split()
txtPrueba = ""
txtPrueba = txtPrueba.join(listaTxt)
txtPrueba = txtPrueba.lower()
if len(txtPrueba) <= 2:
    print("No es un palíndromo")
else:
    palindromo = True
    izq = 0
    der = len(txtPrueba) - 1
    while izq < der and palindromo:
        if ord(txtPrueba[izq]) != ord(txtPrueba[der]):
            palindromo = False
            continue
        izq += 1
        der -= 1
    if palindromo: print("Es un palíndromo")
    else: print("No es un palíndromo")