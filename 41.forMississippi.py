#Escribe un programa que use un ciclo "for" para "contar de forma mississippi" hasta cinco.
#Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final
#"¡Listo o no, ahí voy!"
import time

# Escribe un ciclo for que cuente hasta cinco.
for i in range(5):
    # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    print(i + 1, "Mississippi")
    # Cuerpo del ciclo - uso: time.sleep (1)
    time.sleep(1)
# Escribe una función de impresión con el mensaje final.
print("¡Listo o no, ahí voy!")