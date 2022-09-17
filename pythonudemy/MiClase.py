#varibales de clase 
class MiClase:
	variable_clase = 'Valor variable clase'		

	def __init__(self, variable_instancia):
		self.variable_instancia = variable_instancia

	#metodo estatico de la clase 
	@staticmethod
	def metodo_estatico():# un metodo estatico no puede acceder a laa veriables de instancia 
		print(MiClase.variable_clase)
		#print(varible_clase) 


	@classmethod
	def metodo_clase(cls):
		print(cls.variable_clase)

	def metodo_instancia(self):
		print('---------------------')
		self.metodo_clase()
		self.metodo_estatico()
		print(self.variable_instancia)
		print(self.variable_clase)
		print('---------------------')



#MiClase.metodo_estatico()
#MiClase.metodo_clase()

objeto1 = MiClase('varibale de instancia')
print(objeto1.metodo_clase())
print(objeto1.variable_instancia)
objeto1.metodo_instancia()

