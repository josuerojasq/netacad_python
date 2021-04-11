#La palabra reservada "for" abre el ciclo "for";
#nota - No hay condición después de eso; no tienes que pensar en las condiciones,
#ya que se verifican internamente, sin ninguna intervención.
#Cualquier variable después de la palabra reservada "for" es la variable de control del ciclo;
#cuenta los giros del ciclo y lo hace automáticamente.
#La palabra reservada "in" introduce un elemento de sintaxis que describe el rango de valores posibles
#que se asignan a la variable de control.
#La función "range()" (esta es una función muy especial) es responsable de generar todos los valores deseados
#de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará
#el ciclo con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99;
#nota: en este caso, la función "range()" comienza su trabajo desde 0 y lo finaliza un paso
#(un número entero) antes del valor de su argumento.
#Nota la palabra clave "pass" dentro del cuerpo del ciclo - no hace nada en absoluto;
#es una instrucción vacía : la colocamos aquí porque la sintaxis del ciclo for exige al menos
#una instrucción dentro del cuerpo (por cierto, if, elif, else y while expresan lo mismo).

for i in range (100):
    #hacer algo()
    pass

#El ciclo se ha ejecutado diez veces (es el argumento de la función "range()").
#El valor de la última variable de control es 9 (no 10, ya que comienza desde 0 , no desde 1).
for i in range(10):
    print("El valor de i es actualmente", i)

#En este caso, el primer argumento determina el valor inicial (primero) de la variable de control.
#El último argumento muestra el primer valor que no se asignará a la variable de control.
for j in range (2, 8):
    print("El valor de j es actualmente", j)

#La función "range()" también puede aceptar tres argumentos:
#El tercer argumento es un "incremento": es un valor agregado para controlar la variable en cada giro del ciclo
#(como puedes sospechar, el valor predeterminado del incremento es 1 ).
for k in range(2, 13, 3):
    print("El valor de k es actualmente", k)

#Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las primeras potencias de dos:
pow = 1
for exp in range(9):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 