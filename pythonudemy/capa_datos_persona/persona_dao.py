#creacion de la clase persona dao (data, acces, objeect)
#operaciones crud (create, read, update, delete)
from conexion import Conexion
from persona import Persona
from logger_base import log



class PersonaDAO:
    '''
    DAO(Data Access Object)
    CRUD(Crate-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE idpersona = %s '
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'


    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor: # cursor = Conexion.obntenerCursor()

            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []

            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)

            return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtnerConexion as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada {persona}')
                return cursor.rowcount

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion as conexion:
            with conexion.cursor as cursor:
                valores = (persona.nombre, persona.apllido, persona. email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona agregada {persona}')
                return cursor.rowcount



if __name__ == '__main__':
    people = PersonaDAO.seleccionar()
    for person in people:
        log.debug(person)
