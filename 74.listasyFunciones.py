#¿Se puede enviar una lista a una función como un argumento?
#¡Por supuesto que se puede! Cualquier entidad reconocible por Python
# puede desempeñar el papel de un argumento de función
def sumaDeLista(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum

print(sumaDeLista([5, 4, 3]))

#¿Puede una lista ser el resultado de una función?
#¡Si, por supuesto! Cualquier entidad reconocible por Python puede ser un resultado de función.
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
        #strangeList.append(i)
    return strangeList

print(strangeListFunction(5))