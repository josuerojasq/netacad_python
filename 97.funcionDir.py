#"dir()" - Puede revelar todos los nombres proporcionados a través de un módulo en particular
#El módulo debe haberse importado previamente como un todo
# (es decir, utilizar la instrucción "import module" - "from module" no es suficiente).
import math

for name in dir(math):
    print(name, end="\t")

dir(math)