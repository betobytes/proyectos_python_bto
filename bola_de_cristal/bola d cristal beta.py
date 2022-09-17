# proyecto bola de cristal 
""" este proyecto intenta predecir el precio de los mercados 
	mediante el uso de redes neuronales recurrentes tipo LSTM """


#importamos las librerias 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

from sklearn.preprocessing  import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

#Importamos el dataset de trabajo
dataset_train = pd.read_csv('TSLA.csv')
training_set = dataset_train.iloc[:, 1:2].values

# Escalamos los datos 
sc = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = sc.fit_transform(training_set)

X_train = []
Y_train = []

time_step = 60
m = len(training_set_scaled)

for i in range(time_step, m):
	X_train.append(training_set_scaled[i-time_step:i, 0])
	Y_train.append(training_set_scaled[i,0])

X_train,Y_train = np.array(X_train), np.array(Y_train)

# Redimensionamos la matriz 
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Creamos la RNN

regressor = Sequential()

#Creamos la primera capa y la salida del lstm dropout de regulacion

regressor.add(LSTM(units=50, return_sequences= True, input_shape=(X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

#segunda capa de LSTM Y regulacion de abandono

#regressor.add(LSTM(units=50, return_sequences= True))
#regressor.add(Dropout(0.2))

#tercera capa lstm y regularizacion de abandono

#regressor.add(LSTM(units=50, return_sequences= True))
#regressor.add(Dropout(0.2))

#cuarta capa lstm y regularizacion de abandono 

#regressor.add(LSTM(units=50, return_sequences= True))
#regressor.add(Dropout(0.2))

#agregamos la capa de salida 

regressor.add(Dense(units=1))

#compilamos la red RNN

regressor.compile(optimizer='adam', loss='mean_squared_error')

#adaptacion de la RNN al set de entrenamiento

regressor.fit(X_train, Y_train, epochs=100, batch_size=32)

