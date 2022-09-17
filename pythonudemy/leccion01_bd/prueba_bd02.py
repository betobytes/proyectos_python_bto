#-------------------insertar registros en postgres desdepython-----------------------------
"""import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = 'admin',host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (('alan', 'Turing', 'Aturing@mail.com'),('fernanda','moya','fermoya@mail.com'),('robert','downey','rdowney@mail.com'))
            cursor.executemany(sentencia, valores)
            #   conexion.commit()
            registros_insert = cursor.rowcount
            print(f'Registros insertados: {registros_insert}')

except Exception as e:
    print(f'ocurrio un error de tipo: {e}')

finally:
    conexion.close()
"""
#----------------------------------------------------------------------------------------
#acutalizar varios reistros
import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia  = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
            #valores =(('Julio','chavez','jchavez@mail.com',1),
            #          ('saul','alvarez','salvarez@mail.com',3))
            #para eliinar registros

            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            valores = (7,)
            cursor.execute(sentencia, valores)#--------para un registro
            #cursor.executemany(sentencia,valores)#----para varios registros
            #registros_actualizados = cursor.rowcount
            #print(f'registros actualizados {registros_actualizados}')
            registros_eliminados = cursor.rowcount
            print(f'registros registros eliminados: {registros_eliminados}')

except Exception as e:
    print(f'error de tipo: {e}')

finally:
    conexion.close()
