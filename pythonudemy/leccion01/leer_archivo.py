#lectura de archivo mediante clase open
archivo = open('prueba_uno.txt', 'r')
#print(archivo.read())

#leer algunos caracteres de el archivo
#print(archivo.read(5))
#print(archivo.read(3))

#leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

# iterar nuestro archivo
#for linea in archivo:
#    print(linea)

#leer lineas
#print(archivo.readlines())

#acceder a una linea de la lista
#print(archivo.readlines(1))
#print(archivo.readlines(0))

#abrimos un nuevo archivo
# a - anexar informacion

archivo2 = open('copia.txt', 'a', encoding = 'utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('se a finalizado el proceso de leer y copiar archivos')
