#Cuando usa la variante "from module import name" y se necesita cambiar el nombre de la entidad,
# se crea un alias para la entidad
#La frase "nombre as alias" puede repetirse: emplea "comas" para separar las frases
from math import pi as PI, sin as seno

print(seno(PI/2))