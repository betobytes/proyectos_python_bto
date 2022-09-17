#clase rectangulo 
from FiguraGeometrica import FiguraGeometrica
from color import Color


class Rectangulo(FiguraGeometrica, Color):
	def __init__(self, lado, ancho, color):
		FiguraGeometrica.__init__(self, lado, ancho) #metodo iniciaizador de la clase padre
		Color.__init__(self, color)

	def calcular_area(self):
		return self.ancho * self.alto

	def __str__(self):
		return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

