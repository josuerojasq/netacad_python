#Sudoku es un rompecabezas de colocación de números jugado en un tablero de 9x9.
# El jugador tiene que llenar el tablero de una manera muy específica:
#1. Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
#2. Cada columna del tablero debe contener todos los dígitos del 0 al 9 (nuevamente, el orden no importa).
#3. Cada subcuadro de 3x3 de la tabla debe contener todos los dígitos del 0 al 9
#Escribir un programa que:
#Lea las 9 filas del Sudoku, cada una con 9 dígitos
# (verifica cuidadosamente si los datos ingresados son válidos).
#Da como salida "Si" si el Sudoku es válido y "No" de lo contrario.
#195743862
#431865927
#876192543
#387459216
#612387495
#549216738
#763524189
#928671354
#254938671
def VerificaFila(fila):
    try:
        assert fila.isdigit()
        listaFila = list(fila)
        listaFila.sort()
        for i in range(len(listaFila)):
            if i + 1 != int(listaFila[i]):
                return False
        return True
    except AssertionError:
        print("Debes ingresar una cadena de solo digitos del 1 al 9")
        return False
    except:
        print("Algo salio mal...")
        return False

def VerificaColumnas(tablero):
    listaColumna = []
    columna = ""
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            listaColumna.append(tablero[j][i])
        columna = columna.join(listaColumna)
        if not VerificaFila(columna):
            return False
        del listaColumna[:]
        columna = ""
    return True



i = 0
tablero = []
while i < 9:
    fila = input("Ingresa los valores de la fila "+ str(i + 1) + ": ")
    if VerificaFila(fila):
        tablero.append(fila)
        i += 1
    else:
        print("Debes ingresar todos los digitos del 1 al 9")
        print("Vuelve a ingresar los datos por favor...")
if VerificaColumnas(tablero):
    listaMatriz = []
    matriz = ""
    i = 0
    li = 0
    ls = 3
    cubos = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    while i < len(tablero):

else:
    print("No")
