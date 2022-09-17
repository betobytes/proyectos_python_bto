class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'

        #definimos el metodo get
    @property
    def nombre(self):
        return self._nombre

        #definimos el metodo set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

"""
class Cancion:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Cancion: {self._nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
"""
