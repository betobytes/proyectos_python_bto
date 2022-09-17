class Monitor:
	contador_monitor = 0
	def __init__(self, marca, tamaño):
		Monitor.contador_monitor += 1
		self.id_monitor = Monitor.contador_monitor 
		self.marca = marca
		self.tamaño = tamaño

	def __str__(self):
		return f'Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamaño} pulgadas'


if __name__ == '__main__':

	monitor1 = Monitor('HP', 15)
	print(monitor1)

	monitor2 = Monitor('acer', 27)
	print(monitor2)


