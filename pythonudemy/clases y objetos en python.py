 class Persona:
#atributos
	def __init__(self,nombre,apellido,edad): #metodo de tipo donder 
		self.nombre = nombre #tambien jala con this pero python lo recomienda asi
		self.apellido = apellido
		self.edad = edad

	def mostrar_detalle(self):
		print(f'persona:{self.nombre} {self.apellido} {self.edad}')



persona_uno = Persona('jose','garcia',12)
persona_uno.mostrar_detalle()
persona_dos = Persona('angel','aguilar',18)
persona_dos.mostrar_detalle()

#se pueden agragar datos al vuelo para los objetos pero
#estos no seran compartidos por otros de la misma clase



#print(f'objeto persona 2:{persona_dos.nombre} {persona_dos.apellido} {persona_dos.edad}')
#print(f'objeto persona 1:{persona_uno.nombre} {persona_uno.apellido} {persona_uno.edad}')

#modificar los valores de un objeto ya reado
#persona_uno.nombre = 'juan carlos'
#persona_uno.apellido = 'rodriguez'
#persona_uno.edad = '22'


class Aritmetica:
	"""
  clase aritmetica para realizar operaciones de sumar restar, etc
	"""
	def __init__(self,opreandoA, operandoB):
		self.opreandoA = opreandoA
		self.operandoB = operandoB

	def sumar(self):
		return self.opreandoA + self.operandoB

	def resta(self):
		return self.opreandoA - self.operandoB

	def multiplicacion(self):
		return self.opreandoA * self.operandoB

	def division(self):
		return self.opreandoA / self.operandoB

Aritmetica_uno = Aritmetica(5,3)
print(f'suma: {Aritmetica_uno.sumar()}')
print(f'resta: {Aritmetica_uno.resta()}')
print(f'multiplicacion {Aritmetica_uno.multiplicacion()}')
print(f'division {Aritmetica_uno.division():.3f}')

class Rectangulo:
	def __init__(self,base,altura):
		self.base = base
		self.altura = altura

	def area(self):
		areaa =  self.base * self.altura
		print(f'el area es: {areaa} \n')

b_uno = int(input('ingrese la distancia de la base: '))
a_uno = int(input('ingrese la distncia de la altura: '))


rectuangulo_uno = Rectangulo(b_uno,a_uno)
rectuangulo_uno.area()
#print(f'el area es: {rectuangulo_uno.area()}')

class prlppdo:
	def __init__(self,largo,ancho,alto):
		self.largo = largo
		self.ancho = ancho
		self.alto = alto

	def volumen(self):
		vol = self.largo * self.ancho * self.alto
		print(f'el volmen de la pieza es {vol}\n')

lar = int(input('ingrese el largo de la pieza: '))
anch = int(input('ingrese el ancho de la pieza: '))
alt = int(input('ingrese el alto de la pieza: '))

paralelepipedo1 = prlppdo(lar, anch, alt)
paralelepipedo1.volumen()
