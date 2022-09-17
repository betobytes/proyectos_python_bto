 # eliminar varios registros de una db
import psycopg2

conexion = psycopg2.connect(user='postgres', password = 'admin1',  host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar separado por comas: ')

            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'los registros eliminados son: {registros_eliminados}')


except Exception as e:
    print(f'error de tipo: {e}')

finally:
    conexion.close()
