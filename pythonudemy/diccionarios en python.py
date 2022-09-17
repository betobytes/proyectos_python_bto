#diccionario
#dict(key,value)
dicccionario_uno = {
	'IDE':'intgrate development enviroment',
	'OOP':'object oriented programming',
	'DBMS':'database managment system'
}
print(dicccionario_uno)
#longitud
print(len(dicccionario_uno))
#acceder a un elemento 
print(dicccionario_uno['IDE'])
#acceder a elemento no2
print(dicccionario_uno.get('OOP'))
#Modificar elementos de un diccioneario 
dicccionario_uno['IDE'] = 'entorno de desarrollo integrado'
print(dicccionario_uno)
#recorrer elemtos de un diccionario 
for termino in dicccionario_uno:
	print(termino)

for terminos, valor in dicccionario_uno.items():
 	print(terminos, valor)

for termino in dicccionario_uno.keys():
	print(termino)
for valor in dicccionario_uno.values():
	print(valor)
#comprobar existencia de algun elemento 
print('OOP'in dicccionario_uno)

#agregar elemento a diccionario 
dicccionario_uno['PK'] = 'primari key'
print('\n')
print(dicccionario_uno)
#REMOVER ELEMENTO 
dicccionario_uno.pop('DBMS')
print(dicccionario_uno)
#limpiar el diccionario 
dicccionario_uno.clear()
print(dicccionario_uno)
#para borrar usamos del 
#ejemplo:
#diccionario_uno.del()
