#como crear una funcion

#asi se contruye una funcion
def hola(nombre):
	print("hola mundo")
	print("como esta sr:"+ nombre)
#se invoca llamandola por su nombre
hola("humberto")
hola("babas")
hola("coffy")

#definimos la funcion add()---- agregar
"""def add(numeroUno,numeroDos):
	return numeroUno + numeroDos #el valor que retorna es la suma de los parametros dados a la funcion

print(add(1000, 30))#imprime en consola los parametros que se le pasan a la funcion
"""
#len es una funcion preconstruida por python que me dice el numero de elementos de una varibale o un array

print(len("hola"))

#las funciones lambda son anonimas que toman un numero de argumentos 
#pero que pueden ser escritas con una sola expresion 
""" esto es una funcion que no tiene nombre con dos parametros
pero retorna algo por defecto"""
 
add = lambda number_one, number_two: number_one + number_two 

print(add(100,30)) 
