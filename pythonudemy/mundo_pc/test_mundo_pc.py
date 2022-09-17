#test_mundo_pc
from raton import Raton 
from teclado import Teclado 
from monitor import Monitor
from computadora import Computadora
from orden import Orden 


teclado1 = Teclado('HP', 'USB')
raton1 = Raton('hp', 'usb')
monitor1 = Monitor('hp', 15)
computadora1 = Computadora('hp', teclado1, raton1, monitor1)
	
  
teclado2 = Teclado('Acer', 'bluethoot')
raton2 = Raton('hp', 'bluethoot')
monitor2 = Monitor('hp', 80)
computadora2 = Computadora('alien_ware',teclado2, raton2, monitor2)
	

computadora3 = Computadora('acer', teclado2, raton1, monitor1)

computadoras1 = [computadora1, computadora2]
computadoras2 = [computadora2, computadora3, computadora1]

orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)

print(orden1)
print(orden2)