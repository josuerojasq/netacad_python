#Una excepción concreta que surge cuando el usuario usa un atajo de teclado
# diseñado para terminar la ejecución de un programa (Ctrl-C en la mayoría de los Sistemas Operativos);
# si manejar esta excepción no conduce a la terminación del programa,
# el programa continúa su ejecución. Nota: esta excepción no se deriva de la clase Exception
# Este código no puede ser terminado presionando Ctrl-C
from time import sleep

seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")