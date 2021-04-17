#Solo hay dos tipos de circunstancias en las que None se puede usar de manera segura:
# Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
# Cuando se compara con una variable para diagnosticar su estado interno.

valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor")

def strangeFunction(n):
    if(n % 2 == 0):
        return True

print(strangeFunction(2))
print(strangeFunction(1)) 