#test_polimorfismo 
#polimorfismo 
from EMPLEADO import Empleado
from Gerente import Gerente 

def imprimir_detalles(objeto):
	#print(objeto)
	print(type(objeto))
	print(objeto.mostrar_detalles())
	if isinstance(objeto, Gerente):
		print(f'Departamento: {objeto.departamento}')
	print('\n')

emplado1 = Empleado('juan', 5000)
imprimir_detalles(emplado1)


gerente1 = Gerente('Carlos', 6000, 'sistemas' )
imprimir_detalles(gerente1)
