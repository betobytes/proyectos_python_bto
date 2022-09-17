class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre 
		self.edad = edad

	def __add__(self, otro):
		#return self.nombre + otro.nombre 
		return f'{self.nombre} {otro.nombre}'

	def __sub__(self, otro):
		return self.edad - otro.edad  


persona1 = Persona('juan', 30)
persona2 = Persona('Carlos', 23)
print(persona1 + persona2)
print(persona1 - persona2)


#objeto1 + objeto2 
#obj1._add__(obj2)