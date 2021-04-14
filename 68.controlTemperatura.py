#Imagina que desarrollas una pieza de software para una estación meteorológica automática.
#El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes.
#Esto te da un total de 24 × 31 = 744 valores.
#Intentemos diseñar una lista capaz de almacenar todos estos resultados.

temps = [[0.0 for h in range (24)] for d in range (31)]
#
# la matriz se actualiza mágicamente aquí
#

#Ahora es el momento de determinar la temperatura promedio mensual del mediodía
suma = 0.0

for day in temps:
    suma += day[11]

promedio = suma / 31

print("Temperatura promedio al mediodía:", promedio)

#Ahora encuentra la temperatura más alta durante todo el mes
mas_alta = -100.0

for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp

print("La temperatura más alta fue:", mas_alta)

#Ahora cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:
hotDays = 0

for day in temps:
    if day[11] >= 20.0:
        hotDays += 1

print(hotDays, " fueron los días calurosos.")