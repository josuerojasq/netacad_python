#"__module__" es una cadena, también almacena el nombre del módulo que contiene la definición de la clase.
#Cualquier módulo llamado "__main__" en realidad no es un módulo,
# sino es el archivo actualmente en ejecución.
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__)