#Escribir un programa que puede simular el funcionamiento de un display de siete segmentos,
# aunque vas a usar LEDs individuales en lugar de segmentos.
#Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto),
# así es como lo imaginamos:
def LEDsGenerator(number):
  try:
    global listaLEDs
    number = number.strip()
    assert number.isdigit()
    panel = ""
    for filaLED in range(len(listaLEDs)):
      for digit in number:
        panel = panel + listaLEDs[filaLED][int(digit)] + " "
      panel += "\n"
    return panel
  except AssertionError:
    print("La cadena no es de puro digitos")
  except:
    print("Debes introducir una cadena de digitos")

listaLEDs = [['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###'],
             ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #'],
             ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###'],
             ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #'],
             ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###']]

sw = 83
while sw == 83:
  try:
    numero = input("Ingresa el numero que deseas mostrar en el panel: ")
    print(LEDsGenerator(numero))
    sw = input("Deseas generar otro numero? S/N\n")
    sw = ord(sw)
  except TypeError:
    print("Debes ingresar solo los valores S: Si o N: No")
    sw = input("Deseas generar otro numero? S/N\n")
    sw = ord(sw)
  except:
    print("Ups! Algo salio mal Adios!")