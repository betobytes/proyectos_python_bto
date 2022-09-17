#with open('prueba_uno.txt', 'r', encoding = 'utf8') as archivo:
#    print(archivo.read())

from ManejoArchivos import ManejoArchivos

with ManejoArchivos ('prueba_uno.txt') as archivo:
    print(archivo.read())
