""" ----------existen 3 tipos de modulos en pyhon------------"""
"""los modulos son bloques de codigo preconstruidos que nos
   permiten funcionalidades sin necesidad de reinventar la ruda"""
# modulos propios
# modulos de otros que descargamos 
# modulos que trae python por default


#para ver la lista de los modulos en python se pueden googlear--- mediante module python index
#buscar modulos de empresas mediante pip modules nos da una lista de modulos fabricados por la comunidad

####### forma una de importar una funcion de un modulo
"""
import datetime
print("el dia de hoy es ")
print(datetime.date.today())
print(datetime.timedelta(minutes=700))

#forma mas elegante de importar una funcion de un modulo 

#from datetime import timedelta--->para 1 dato
 """
#from datetime import timedelta, date #### asi se importan 2 datos 

#print(timedelta(minutes = 12))
#print(date.today())

#forma 1

    #import fmath

    #fmath.add(3,4)
    #fmath.resta(3,4)

#forma 2
from fmath import add, resta

resta(2,5)### _______________cuando se use este metodo recuerde la sangri todo alineado a la izq
add(8,3)    

from colorama import Fore,Style, init
init(convert = True)

print(Fore.RED+"hola mundo ")# imprimira en rojo  hola mundo 