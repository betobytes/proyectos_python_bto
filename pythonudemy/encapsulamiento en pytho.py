#encapsulamiento en pytho 
class Person:
	def __init__(self,nombre,apellido,edad):
		self._nombre = nombre
		self._apellido = apellido
		self._edad = edad
		#self.valores = valores
		#self.terminos = terminos

	@property
	def nombre(self):
		print('llamando al metodo get nombre')
		return self._nombre
	
	@nombre.setter
	def nombre(self, nombre):
		print('llamando al metodo set nombre')
		self._nombre = nombre
	
	@property
	def apellido(self):
		
		return self._apellido
	
	@apellido.setter
	def apellido(self, apellido):
		
		self._apellido = apellido
	
	@property
	def edad(self):
		
		return self._edad
	
	@edad.setter
	def edad(self, edad):
		
		self._edad = edad 
		

	def mostrar(self):
		print(f'{self._nombre} {self._apellido} {self._edad} ')
#nombre_usuario = input('ingrese su nombre: ')
#apellido_usux|ario = input('ingrese su apellido: ')
#edad_usuario = int(input('ingrse su edad: '))
#num_usuario = int(input('ingrse su numero'))

#persona1 = Person(nombre_usuario, apellido_usuario, edad_usuario, '4445553322',2,3,5, m=manzana, p=pera,)
#persona1 = Person('Juan','Perez',28,'4445553322',2,3,5, m='manzana' ,p='pera')

persona1 = Person('juan','torres',40)
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'perez'
persona1.edad = '30'
persona1.mostrar()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

