#Escribir y probar una función que toma un argumento (un año)
#y devuelve True si el año es un año bisiesto, o False sí no lo es.
def isYearLeap(year):
    result = None
    if year >= 1582:
        if (year % 4) != 0: result = False
        elif (year % 100) != 0: result = True
        elif (year % 400) != 0: result = False
        else: result = True
    return result

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

#Escribir y probar una función que toma dos argumentos (un año y un mes)
#Y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year,
#tu función debería ser universal).
#La parte inicial de la función está lista. Ahora, haz que la función devuelva "None"
#si los argumentos no tienen sentido.
def daysInMonth(year, month):
    month -= 1
    diasMes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = None
    if (month < len(diasMes)) and (month >= 0):
        if month == 1:
            if isYearLeap(year): result = diasMes[month][1]
            else: result = diasMes[month][0]
        else: result = diasMes[month]
    return result

testYears = [1900, 2000, 2016, 1987, 2018]
testMonths = [2, 2, 1, 11, 14]
testResults = [28, 29, 31, 30, None]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

#Escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes)
#y devuelve el día correspondiente del año, o devuelve "None" si cualquiera de los argumentos no es válido.
def dayOfYear(year, month, day):
    N = None
    if daysInMonth(year,month) and day > 0 and day <= daysInMonth(year,month):
        if isYearLeap(year): K = 2
        else: K = 1
        N = ((275 * month) // 9) - K * ((month + 9) // 12) + day - 30
    return N

print(dayOfYear(2000, 12, 31))
print(dayOfYear(2000, 2, 15))
print(dayOfYear(2018, 8, 27))
print(dayOfYear(2000, 15, 43))