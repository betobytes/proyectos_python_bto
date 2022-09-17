import  psycopg2

conexion = psycopg2.connect(user = 'postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'test_db')

"""#print(conexion)
#un cursor es un objeto que permite ejecutar sentencias sql en postgres
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
#recuperamos los registros mediante el metodo fetchall
#fethall permite recuperar los registros e la sentencia
registro = cursor.fetchall()
print(registro)

cursor.close()
conexion.close()
"""
try:
    with conexion:
        with conexion.cursor() as cursor:
            instruccion = 'SELECT * FROM persona WHERE id_persona IN %s'
            #%s placeholder parametro posicional
            #llaves_primarias = ((1,2,3),)
            entrada = input('proporcione los id separado por comas: ')
            llaves_primarias = (tuple(entrada.split(',')), )
            #id_persona = int(input('proporcione el valor del id_persona: '))
            #cursor.execute(instruccion, (id_persona, ))
            cursor.execute(instruccion, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            #para regresar solo un registro

except Exception as e:
    print(f'ocurrio un error: {e}')

finally:
    conexion.close()


#para convertir una variable en un tupla (var,)
