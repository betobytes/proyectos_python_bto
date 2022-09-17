# herencia en python 
# clase padre 
#super().__init__()
#super().__str__()
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad 

	def __str__(self):# regrea un string con los atributos de nustra clase 
		return f'Persona: Nombre:{self.nombre} Edad:{self.edad} '

#herencia clase hijo 
class Empleado(Persona):
	def __init__(self,nombre, edad, sueldo):
		super().__init__(nombre, edad)
		self.sueldo = sueldo

	def __str__(self):
		return f'{super().__str__()} Sueldo:{self.sueldo}'



