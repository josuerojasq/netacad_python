#isinstance(): isinstance(nombreObjeto, nombreClase)
#La función devuelve True si el objeto es una instancia de la clase, o False de lo contrario.
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()