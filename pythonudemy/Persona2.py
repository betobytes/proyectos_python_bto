#clase perona con contador 
class Persona:
	contador_personas = 0
	
	@classmethod
	def generar_siguiente_valor(cls):
		cls.contador_personas += 1
		return cls.contador_personas


	def __init__(self, nombre, edad):
		#Persona.contador_personas += 1
		#self.id_persona  = Persona.contador_personas
		self.id_persona = Persona.generar_siguiente_valor()
		self.nombre = nombre
		self.edad = edad

	def __str__(self):
		return f'Persona [{self.id_persona}, {self.nombre}, {self.edad}]'


persona1 = Persona('juan', 35)
print(persona1)
persona2 = Persona('carlos', 40)
print(persona2)
persona3 = Persona('fernanda', 24)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona('mia', 30)
print(persona4)
print(f'valor contador personas: {Persona.contador_personas}')
