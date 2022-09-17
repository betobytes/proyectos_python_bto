#clase cuadrado 
from FiguraGeometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
	def __init__(self, lado, color):
		#super().__init__
		FiguraGeometrica.__init__(self, lado, lado)
		Color.__init__(self, color)		
		
	def calcular_area(self):
		#acceiendo a los atributos de la clase padre
		return self.alto * self. ancho

	def __str__(self):
		return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)} '

""""class Rectangulo(FiguraGeometrica, Color):
	def __init__(self, ancho, alto, color):
		FiguraGeometrica.__init__(self, ancho, alto)
		Color.__init__(self, color)

	def calcular_area(self):
		return self.alto * self.ancho

	def __str__(self):
		return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
""" 

"""
cuadrado1 = Cuadrado(4, 'azul')

#print(cuadrado1.ancho)
#print(cuadrado1.alto)
#print(cuadrado1.color)
print('creacion de objeto cuadrado'.center(50,'-'))
print(f'calculo del area de un cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)
print('\n')

# METODO ORDEN DE RESOLUCION (metod resolucion order)
print(Cuadrado.mro())
print('\n')

print('creacion de objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(3, 8,'verde')
print(f'el calculo del area de un rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
"""