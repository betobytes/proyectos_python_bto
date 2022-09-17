
class Orden:
	contador_ordenes = 0 

	def __init__(self, computadoras):
		Orden.contador_ordenes += 1
		self.id_ordenes = Orden.contador_ordenes
		self.computadoras = computadoras

	def agregar_computadoras(self, computadora):
		self.computadoras.append(computadora)

	def __str__(self):
		computadoras_str = ''

		for computadora in self.computadoras:
			computadoras_str += computadora.__str__()

		return f'Orden:  {self.id_ordenes}\n   computadoras : {computadoras_str}\n '

