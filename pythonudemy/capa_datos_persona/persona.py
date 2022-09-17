#clase persona
from logger_base import log
class Persona:
    def __init__(self, id_persona = None, nombre = None, apellido = None, email=None):
        self._id_persona  = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    #el metodo str muestra el contenido de las variables de clase
    def __str__(self):
        return f'''
            id_persona : {self._id_persona},
            nombre: {self._nombre},
            apellido: {self._apellido},
            email: {self._email}
        '''
    #metodo get
    @property
    def id_persona(self):
        return self._id_persona
    #metodo set
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
    #metdo get para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    #metodo get para apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    #metodo get para email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    persona_uno = Persona(1, 'Juan', 'Perez', 'j@perezmail.com')
    log.debug(persona_uno)
    #simular un insert
    persona_dos = Persona(nombre= 'juan', apellido = 'Perez', email = 'jperez@mail.com')
    log.debug(persona_dos)
    #simular un delete o una eliminacion
    persona_uno = Persona(id_persona = 1)
    log.debug(persona_uno)

    for i in range(97, 100):
        print(chr(i))
