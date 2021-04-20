#Escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario.
# Para hacerlo más fácil, Hemos decidido simplificar el juego. Aquí están nuestras reglas:
#
#La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
#El usuario (por ejemplo, tu) jugará utilizando las 'O's.
#El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
#Todos los cuadros están numerados comenzando con el 1.
#El usuario ingresa su movimiento introduciendo el numero de cuadro elegido.
# El numero debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10,
# y no puede ser un cuadro que ya esté ocupado.
#El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos:
# el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
#La maquina responde con su movimiento y se verifica el estado del juego.
#No se debe implementar algún tipo de inteligencia artificial,
# la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
#El tablero debe ser almacenado como una lista de tres elementos,
# mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas)
# de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:
#"board[fila][columna]"
# Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito
# representando el número del cuadro (dicho cuadro se considera como libre).
#Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python
# denominada "randrange()"
#La instrucción "from-import" provee acceso a la función "randrange" definida en un módulo externo
# de Python denominado "random".
from random import randrange

def DisplayBoard(board):
    print("""
+-------+-------+-------+
|       |       |       |
|   """+ str(board[0][0]) +"""   |   """+ str(board[0][1]) +"""   |   """+ str(board[0][2]) +"""   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   """+ str(board[1][0]) +"""   |   """+ str(board[1][1]) +"""   |   """+ str(board[1][2]) +"""   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   """+ str(board[2][0]) +"""   |   """+ str(board[2][1]) +"""   |   """+ str(board[2][2]) +"""   |
|       |       |       |
+-------+-------+-------+
""")
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola

def EnterMove(board):
    global coordDict
    sw = True
    while sw:
        userMove = int(input("Ingresa tu movimiento: "))
        if userMove > 0 and userMove < 10:
            coordSelect = coordDict[userMove]
            if coordSelect in MakeListOfFreeFields(board):
                board[coordSelect[0]][coordSelect[1]] = "O"
                sw = False
            else:
                print("Cuadro oupado! Ingresa el valor de un cuadro libre")     
        else:
            print("Por favor ingresa un valor válido en el rango de 1 - 9")
    return board
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario

def MakeListOfFreeFields(board):
    freeList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if type(board[i][j]) == int:
                coordTuple = (i, j)
                freeList.append(coordTuple)
    return freeList
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna

def VictoryFor(board, sign):
    sw = False
    if len(MakeListOfFreeFields(board)) <= 4:
        for i in range(len(board)):
            if (board[i][0] == board[i][1] == board[i][2] == sign) or \
                (board[0][i] == board[1][i] == board[2][i] == sign) :
                sw = True
        if (board[0][0] == board[1][1] == board[2][2] == sign) or \
            (board[2][0] == board[1][1] == board[0][2] == sign) :
            sw = True
    return sw
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego

def DrawMove(board):
    global coordDict
    sw = True
    while sw:
        machineMove = randrange(1,9)
        coordSelect = coordDict[machineMove]
        if coordSelect in MakeListOfFreeFields(board):
            board[coordSelect[0]][coordSelect[1]] = "X"
            sw = False
    return board

# la función dibuja el movimiento de la maquina y actualiza el tablero

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
coordDict = {
    1:(0, 0), 2:(0, 1), 3:(0, 2),
    4:(1, 0), 5:(1, 1), 6:(1, 2),
    7:(2, 0), 8:(2, 1), 9:(2, 2),
    }

print(
"""
+==================================+
| Bienvenido a Tic-Tac-Toe!        |
| Demuestra tus habilidades        |
| intentado vencer a Robotin       |
| El ya inicio el juego.           |
| Entonces,                        |
| ¿Aceptas el desafio?             |
| Si >> Acepto el desafio          |
| No >> Salir del Juego            |
+==================================+
""")
game = input()

while game in ["Si", "si"]:
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    coordDict = {
    1:(0, 0), 2:(0, 1), 3:(0, 2),
    4:(1, 0), 5:(1, 1), 6:(1, 2),
    7:(2, 0), 8:(2, 1), 9:(2, 2),
    }
    bandera = [False,""]
    restMov = 8
    while not bandera[0] and restMov > 0:
        DisplayBoard(board)
        if restMov % 2 == 0:
            board = EnterMove(board)
            if VictoryFor(board, "O"):
                bandera[0] = True
                bandera[1] = "User"
        else:
            board = DrawMove(board)
            print("¡Robotin a jugado!")
            if VictoryFor(board,"X"):
                bandera[0] = True
                bandera[1] = "Machine"
        restMov -= 1
    DisplayBoard(board)
    if bandera[1] == "User":
        print("¡Has Ganado!")
    elif bandera[1] == "Machine":
        print("¡Has Perdido!")
    else:
        print("¡Hemos Empatado!")
    print(
    """
+==================================+
| ¿Continuamos?                    |
| Si >> Iniciar otra ronda         |
| No >> Salir del Juego            |
+==================================+
""")
    del board
    game = input()

print(
"""
+==================================+
|          ¡Hasta Pronto!          |
+==================================+
""")