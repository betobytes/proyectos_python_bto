#clase teclado 
from dispositivo_entrada import Dispositivo_entrada

class Teclado(Dispositivo_entrada):

	contador_teclado = 0

	def __init__(self, marca, tipo_entrada):
		Teclado.contador_teclado += 1
		self.id_teclado = Teclado.contador_teclado
		super().__init__(marca, tipo_entrada)
       
	def __str__(self):
		return f'Id: {self.id_teclado} Marca: {self._marca}, tipo_entrada: {self._tipo_entrada}'

if __name__ == '__main__':

	teclado1 = Teclado('HP', 'USB')
	print(teclado1)
	teclado2 = Teclado('gamer', 'Bluethoot ')
	print(teclado2)

