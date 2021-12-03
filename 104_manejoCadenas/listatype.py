#Dada la lista:
#lista2 = [1,3, 'cadena', 4, 'vvvv', 7, 'bamboo', 0, 'ratones', 'celular']
#Mostrar los elementos siguiendo las reglas:
#Si el elemento es de tipo cadena mostrar “Es una cadena y vale {valor de la
#cadena}”
#Si el elemento es un número mostrar el elemento correspondiente al valor del
#elemento. Por ejemplo si es 4 mostrará “vvvv”
#Ayuda: Puede usar la funcion type(valor), si valor es una cadena type retornará
#<class ‘str’>

lista = [1.3, 4, 'cadena', 'vvvv', 7, 'bamboo', 0, 'ratones', 'celular']

for elem in lista:
    if type(elem) is str:
        print("Es una cadena y vale: " + elem)
    elif type(elem) is int:
        valor = ""
        for elem2 in lista:
            if type(elem2) is str and elem == len(elem2):
                valor = valor + " " + elem2
        print(elem, valor)
    else:
        continue


