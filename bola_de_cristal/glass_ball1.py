"""---------------PROYECTO BOLA DE CRISTAL----------------------
vamos a predecier el precio de las acciones y los mercados haciendo uso de 
redes neuronales recurrentes de tipo LSTM(long short therm memori) y lenguaje 
de programacion python 

.... SE REQUERIRAN LA LIBRERIAS 
...numpy:______________manejo de matrices
...matplotlib.pyplot:__realizacion de graficos
...pandas:_____________realizacion de dataframes
...scitkit learn:______realizacion de modelos de mchine learning
...keras:______________realizacion de neural networks

"""

import numpy as np 
np.random.seed(4)
import matplotlib.pyplot as plt
import pandas as pd 

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM 



# Creamos una funcion auxiliar para graficar los datos 

def graficar_predicciones(real, prediccion):
	plt.plot(real[0:len(prediccion)], color='skyblue', label='valor de la accion real')
	plt.plot(prediccion, color='salmon', label='predccion del precio de la accion')
	plt.ylim(1.1 * np.min(prediccion)/2, 1.1 * np.max(prediccion))
	plt.xlabel('tiempo')
	plt.ylabel('valor de la accion')
	plt.legend()
	plt.show()

#creamos nuestro dataset de trabajo

ds_precio = pd.read_csv('EURUSD=X.csv', index_col= 'Date', parse_dates= ['Date'])
ds_precio.head()


# Sets de entrenamiento y validacion 
# La LSTM se entrenara con datos del 2019 hacia atras y la validacion con datos del 2020 en adelante 
# en ambos casos usaremos el valor de cierre por cada dia 


set_entrenamiento = ds_precio[:'2019'].iloc[:, 1:2]
set_validacion = ds_precio['2020':].iloc[:, 1:2]


set_entrenamiento['High'].plot(legend=True)
set_validacion['High'].plot(legend=True)
plt.legend(['Entrenamiento(2019-2020)','Validacion[2020-2021]'])


# Normalizacion del set de entrenamiento 

sc = MinMaxScaler(feature_range=(0,1))
set_entrenamiento_escalado = sc.fit_transform(set_entrenamiento)


# La red LSTM tendra como entrada 'time_step' datos consecutivos, y como salida 1 dato (la prediccion 
# a partir de esos "time_step"). Se conformara de esta forma el set de entrenamiento 

time_step = 60 # periodos que vamos a analizar para entrenar la red 
X_train = []
Y_train = []
m = len(set_entrenamiento_escalado)


for i in range(time_step, m):

	#X: bloques de entrenamiento "time_step" datos:  0- time_step, 1- time_step+1, 2- time_step+2, etc
	X_train.append(set_entrenamiento_escalado[i-time_step:i, 0])

	#Y: el siguiente dato 
	Y_train.append(set_entrenamiento_escalado[i,0])


X_train, Y_train =  np.array(X_train), np.array(Y_train)

# Redimensionamos la matriz para que se ajuste al modelo en keras

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

#contruimos la red LSTM(Long- Short Therm Memorie)

dim_entrada = (X_train.shape[1], 1)
dim_salida = 1 
na = 50 #numero de  neuronas  

modelo = Sequential()
modelo.add(LSTM(units=na, input_shape=dim_entrada))
modelo.add(Dense(units=dim_salida))
modelo.compile(optimizer='rmsprop', loss='mse')
modelo.fit(X_train, Y_train, epochs= 20, batch_size=32)


# Validacion (prediccion del valor de la acciones)

x_test = set_validacion.values
x_test = sc.transform(x_test)

X_test = [] 

for i in range(time_step, len(x_test)):
	X_test.append(x_test[i-time_step:i,0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1],1))

prediccion = modelo.predict(X_test)
prediccion = sc.inverse_transform(prediccion)


# Graficamos lo resultados pasandolos a la funcion 
graficar_predicciones(set_validacion.values, prediccion)

