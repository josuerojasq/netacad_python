#Las cadenas de Python son secuencias. Es hora de mostrarte lo que significa realmente.
#Las cadenas no son listas, pero pueden ser tratadas como tal en muchos casos.
exampleString = 'silly walks'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')

print('\n')

#Iterar a través de las cadenas funciona también.
for ch in exampleString:
    print(ch, end=' ')

print()