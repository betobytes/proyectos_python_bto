#transacciones bases de datos

#una transaccion es una consulta que modifica la base de datos
#por lo tanto varias transacciones hacen varias modificaciones
import psycopg2 as bd

conexion = bd.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database = 'test_db')

try:
    #no se recomieda el autocommit fuera de las pruebas
    conexion.autocommit = False #autocommit significa que se guarde de forma automatica los cambios
    cursor = conexion.cursor()
    sentencia = ('INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)')
    valores = ('steve','rogers','srogers@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()#guarda los camios realizaos en la database
    #es aconsejable guardar el commit manualmente
    print('Termina la transaccion exitosamente')

except Exception as e:
    conexion.rollback() #si algo sale mal le da para atras a los cambios
    print(f'ocurrio un error se hizo rollaback de la transaccion: {e}')

finally:
    conexion.close()
