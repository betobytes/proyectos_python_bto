import os
class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'
    #metodo de clase
    @classmethod #puede acceder a los atributos de la clase
    def agregar_pelicula(cls,pelicula):
        with open(cls.ruta_archivo, 'a', encoding = 'utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    #metodo de listar peliculas
    @classmethod #decorador para la definicion del metodo de clase
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding = 'utf8') as archivo:
            print('Catalogo de Peliculas'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'\nArchivo eliminado: {cls.ruta_archivo}\n')
    #no entendi una papa repasar



"""
class Biblioteca:
    ruta_biblioteca = 'musica.txt'

    @classmethod
    def agregar_cancion(cls, cancion):
        with open(cls.ruta_biblioteca, 'a', encoding = 'utf8') as archivo:
            archivo.write(f'{cancion.nombre}\n')

    @classmethod
    def lista_canciones(cls):
        with open(cls.ruta_biblioteca, 'r', rencoding = 'utf8') as archivo:
            print('lista de canciones'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_cancion(cls):
        os.remove(cls.ruta_biblioteca)
        print(f'archivo eliminado: {cls.ruta_biblioteca}\n')
    """
