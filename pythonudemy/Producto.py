#diseño de clases en python 
class Producto:
	contador_productos = 0

	def __init__(self, nombre, precio):
		Producto.contador_productos += 1
		self.id_producto = Producto.contador_productos
		self.nombre = nombre
		self._precio = precio

	@property
	def precio(self):
		return self._precio
	

	def __str__(self):
		return f'Id Producto:{self.id_producto}, Nombre:{self.nombre}, Precio:{self.precio}'

if __name__ == '__main__':
	producto1 = Producto('camisa', 100.00)
	producto2 = Producto('pantalon', 150.00)
	print(producto1)
	print(producto2)


