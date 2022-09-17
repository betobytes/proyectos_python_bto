from dispositivo_entrada import Dispositivo_entrada

class Raton(Dispositivo_entrada):
	
	contador_ratones = 0
	
	def __init__(self, marca, tipo_entrada):
		Raton.contador_ratones += 1
		self.id_raton = Raton.contador_ratones
		super().__init__(marca, tipo_entrada)

	def __str__(self):
		return f'Id: {self.id_raton} Marca: {self._marca}, tipo entrada: {self._tipo_entrada}'


if __name__ == '__main__':

	raton1 = Raton('hp','USB')
	print(raton1)

	raton2 = Raton('acer', 'bluethoot')
	print(raton2)
	