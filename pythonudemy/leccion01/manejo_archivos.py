#manejo de archivos en python
#open() puede leer escribir o crear nuevos archivos
try:
    archivo = open('prueba_uno.txt', 'w', encoding = 'utf8')
    archivo.write('agregamos informacion al archivo \n')
    archivo.write('adios')

except Exception as e:
    print(e)
finally:
    archivo.close()
    print('fin del archivo')
    # archivo.write('nueva info')
