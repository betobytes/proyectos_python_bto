#para este manejo de transacciones utilizaremos with
#asi evitaremos el usto de autocommit

import psycopg2 as bd

conexion = bd.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = ('INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)')
            valores = ('carlos', 'torres', 'ctorres@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = ('UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s ')
            valores = ('Juan', 'Perez', 'jperez@mail.com',1)
            cursor.execute(sentencia, valores)


except Exception as e:
    print(f'ocurrio un error de tipo {e}, se hizo rollback')

finally:
        conexion.close()
print('termina la transaccion, se hizo commit')
