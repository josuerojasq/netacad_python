#"while"
#La rama else del ciclo siempre se ejecuta una vez,
#independientemente de si el ciclo ha entrado o no en su cuerpo.
i = 1
while i < 5:
    print (i)
    i += 1
else:
    print("else:", i)

#for
#La variable i conserva su último valor.
#Nota: si la variable de control no existe antes de que comience el ciclo,
#no existirá cuando la ejecución llegue a la rama else.
for i in range(5):
    print(i)
else:
    print("else:", i)

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i) 