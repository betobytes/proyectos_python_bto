#trading algoritmico 
import pandas as pd 
import requests
import sqlalchemy as sql #para conectarse a la base de datos 
import datetime
import time

def extract_bitso_api():

	response  = request.get('https://api.bitso.com/v3/trades/?book=btc_mxn')
	json_response  = response.json() #

	datos = json_response['payload']
	df = pd.DataFrame(datos)

	engine = sql.create_engine('mysql+mysqlconnector://root:root@localhost/bitso_api')

	initial_q = """INSERT INTO bitso trades
	(book,created_at,amount,maker_side,price,tid)
	VLAUES
	"""

	values_q = ",".join(["""('{}','{}','{}','{}','{}','{}')""".format(
	
					row.book,
					row.created_at,
					row.amount,
					row.maker_side,
					row.price,
					row.tid) for idx, row in df.iterrows()])

	end_q = """ON DUPLICATE KEY UPDATE
			book = values(book),
			created_at = values(created_at),
			amount = values(amount),
			maker_side = values(maker_side),
			price = values(price),
			tid = values(tid);"""

	query = initial_q + values_q

	engine.execute(query)

	return None 

while True :
	extract_bitso_api()
	print('Actualizando DB a las {}'.format(datetime.today()))
	time.sleep(12)



#-------------------------------------------------


datos = []
class muneca:
	def __init__(angulo,fuerza,vel)
	self.fuerza = fuerza
	self.angulo = angulo
	self.vel = vel

class hombro:
	def __init__(angulo,fuerza,vel)
	self.fuerza = fuerza
	self.angulo = angulo
	self.vel = vel

class codo:
	def __init__(angulo,vel)
	
	self.angulo = angulo
	self.vel = vel

class brazo:
	def __init__(angulo,fuerza,vel)
	self.fuerza = fuerza
	self.angulo = angulo
	self.vel = vel


class antebrazo:
	def __init__(angulo,fuerza,vel)
	self.fuerza = fuerza
	self.angulo = angulo
	self.vel = vel

class dedo:
	def __init__(angulo,fuerza,vel)
	self.fuerza = fuerza
	self.angulo = angulo
	self.vel = vel


while True:
