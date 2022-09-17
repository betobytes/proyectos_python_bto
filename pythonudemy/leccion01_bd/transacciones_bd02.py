#transacciones python postgres sql_2
import psycopg2 as bd

conexion = bd.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia  = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('maria', 'mercedes', 'mamercedes@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('maria', ' del_barrio', 'mabarrio@mail.com', 6)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('termino la transaccion exitosamente')

except Exception as e:
    conexion.rollback()
    print(f'ocurrio un error rollback aplicado {e}')

finally:
    conexion.close()
