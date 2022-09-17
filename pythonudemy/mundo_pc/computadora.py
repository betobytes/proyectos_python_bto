from teclado import Teclado 
from raton import Raton
from monitor  import Monitor  


class Computadora:
	contador_computadora = 0

	def __init__(self, nombre, monitor, teclado, raton):
		Computadora.contador_computadora += 1

		self.id_computador = Computadora.contador_computadora
		self.nombre = nombre
		self.monitor = monitor 
		self.teclado = teclado
		self.raton = raton 

	def __str__(self):
		return f'{self.nombre}: {self.id_computador} \n  MONITOR: {self.monitor}\n  TECLADO: {self.teclado}\n   RATON: {self.raton}\n'


if __name__ == '__main__':

	teclado1 = Teclado('HP', 'USB')
	raton1 = Raton('hp', 'usb')
	monitor1 = Monitor('hp', 15)
	computadora1 = Computadora('hp', teclado1, raton1, monitor1)
	print(computadora1)

	teclado2 = Teclado('Acer', 'bluethoot')
	raton2 = Raton('hp', 'bluethoot')
	monitor2 = Monitor('hp', 80)
	computadora2 = Computadora('alien_ware',teclado2, raton2, monitor2)
	print(computadora2)

	computadora3 = Computadora('acer', teclado2, raton1, monitor1)
	print(computadora3)