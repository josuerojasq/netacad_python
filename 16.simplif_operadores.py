#Operadores Abreviados
#Si op es un operador de dos argumentos (esta es una condición muy imporante) 
#y el operador es utilizado en el siguiente contexto:
#"variable = variable 'op' expresión"
#Puede ser simplificado de la siguiente manera:
#"variable 'op'= expresión"

i = 5
j = 10
i += 2 * j
print(i)

var = 15
var /= 2
print(var)

rem = 555
rem %= 10
print(rem)

j -= (i + var + rem)
print(j)

x = 3
x **= 2
print(x)