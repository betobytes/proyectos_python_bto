#FUNCIONES EN PYTHON 

def mi_funcion(nombre,apellido):
	print('\nhola desde funcion')
	print(f'Nombre:{nombre} Apellido:{apellido}')


mi_funcion('jose','perez')
mi_funcion('humberto','muñoz')
#def suma(a:int = 0, b:int = 0) -> int: sintaxis completa de la funcion pero redundante 
def resta(a = 0, b = 0):
	return a - b 
def sumar(a,b):
	return a+b 

resultado = sumar(3, 4)

print(f'resultado de la suma={resultado}')
print(f'reslutado de forma directa {sumar(5, 6)}')
print(f'resultao de la resta {resta()}')
print(f'resultado de resta {resta(4, 3)}')


def listaNombres(*nombres):
	for n in nombres:
		print(n)

listaNombres('hugo','paco','luis')
listaNombres('angus','adam')

#diccionarios en una funcion 
def listaTerminos(**terminos):
	for llave, valor in terminos.items():
		print(f'{llave}:{valor}')

listaTerminos(IDE='integrated development enviroment',PK='primary key')
listaTerminos(DBM='database management system')

def desplagarNombres(nombres):
	for nombre in nombres:
		print(nombre)

nombres = ['juan','karla', 'guillermo']
desplagarNombres(nombres)
desplagarNombres('carlos')
desplagarNombres((10,12))
print('\n')

#funciones recursivas 
#numeros factoriales 

def factorial(num):
	if num == 1:
		return 1 #el punto de quiebre es escencial para que exista un regreso de las funciones 
	else:
		return num * factorial(num-1)

resultado = factorial(5)
print(f'el factorial de 5 es {resultado}')



