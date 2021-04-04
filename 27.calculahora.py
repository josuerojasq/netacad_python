#La tarea es preparar un código simple para evaluar o encontrar el "tiempo final"
#de un periodo de tiempo dado, expresándolo en horas y minutos.
#Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola.
# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
#Obtenemos las horas de duracion
hora_dura = dura // 60
#Obtenemos los minutos de duracion
min_dura = dura % 60

#print("Horas de duracion: " + str(hora_dura))
#print("Minutos de duracion: " + str(min_dura))
print("El evento inicia a hrs. " + str(hora) + ":" + str(min))
print("El evento termina a hrs. " + str(((hora + hora_dura + ((min + min_dura) // 60)) % 24)) + ":" + str((min + min_dura) % 60))