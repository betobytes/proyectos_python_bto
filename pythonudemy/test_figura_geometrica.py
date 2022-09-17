from cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

#no se pueden instanciar una clase abstracta 
#firgura = FiguraGeometrica()

print('creacion objeto cuadrado'.center(50,'-'))
cuadrado1  = Cuadrado(5, 'rojo')
cuadrado1.alto = 9        #quitar el metodo setter implica restricciones en la modificacion de los datos de la clase 
cuadrado1.ancho = cuadrado1.alto
print(f'Calculo area de cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)
print(Cuadrado.mro())
print('\n')

print('creacion objeto rectngulo'.center(50,'-'))
rectangulo1 = Rectangulo(15, 8,'verde')
print(f'calcular area de rectngulo: {rectangulo1.calcular_area()}')
print(rectangulo1)
print(Rectangulo.mro())
