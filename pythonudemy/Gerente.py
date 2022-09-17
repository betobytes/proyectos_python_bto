from EMPLEADO import Empleado


class Gerente(Empleado):
	def __init__(self, nombre, sueldo, departamento):
		super().__init__(nombre,sueldo)
		self.departamento = departamento

	def __str__(self):
		return f'Gerente {super().__str__()} [Departamento: {self.departamento}] '


