#Escribir un programa que:
#Le pida al usuario dos textos por separado.
#Compruebe si los textos ingresados son anagramas e imprima el resultado.
#Nota:
#Supongamos que dos cadenas vacías no son anagramas.
#Tratar las letras mayúsculas y minúsculas como iguales.
#Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
def cleanTxt(text):
    listaTxt = text.split()
    txtClean = ""
    txtClean = txtClean.join(listaTxt)
    txtClean = txtClean.lower()
    listaTxt = list(txtClean)
    listaTxt.sort()
    txtClean = ""
    txtClean = txtClean.join(listaTxt)
    return txtClean

def verifAnagrama(text1, text2):
    text1 = cleanTxt(text1)
    text2 = cleanTxt(text2)
    if text1 == text2: return True
    else: return False


texto1 = input("Ingrese texto 1: ")
texto2 = input("Ingrese texto 2: ")
if verifAnagrama(texto1, texto2):
    print("Anagramas")
else:
    print("No son Anagramas")