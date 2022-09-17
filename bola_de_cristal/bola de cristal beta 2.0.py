#bola de cristal beta 2.0
import math
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

from sklearn.preprocessing  import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

#importamos el dataset de trabajo
df = pd.read_csv('TSLA.csv')
#training_set = df.iloc[:, 1:2].values
#----------------print(df)----------------------

df.shape
#plt.figure(figsize=(16,8))
#plt.title('close price history')
#plt.plot(df['Close'])
#plt.xlabel('Date',fontsize=18)
#plt.ylabel('price',fontsize=18)
#plt.show()

#crear el datafreme solo para cierres
data= df.filter(['Close'])
#convertir el dataframe a numpy
dataset = data.values
# obtenemos el numero de columnas para entrenar el modelo
training_data_len = math.ceil(len(dataset)* 0.8)

#------------------print(training_data_len)-----------------------

#escalamos los datos 
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)



#creamos el dataset de entrenamiento
#creamos el set de entrenamiento escalado 
train_data = scaled_data[0:training_data_len, :]

#dividimos los datos en stes de datos x_trian , y_train
x_train = []
y_train = []

for i in range(60, len(train_data)):
  x_train.append(train_data[i-60:i,0])
  y_train.append(train_data[i,0])
 

#convertimos  el x_train y y_train en un array 
x_train, y_train = np.array(x_train), np.array(y_train)

#Redimensionamos los datos de vector a una matriz  
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1],1))


# construimos el modelo LSTM
model = Sequential()
model.add(LSTM(60, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(60, return_sequences=False))
model.add(Dense(1))


#compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')


#entrenamos el modelo 
model.fit(x_train, y_train, batch_size=80, epochs=80)


#creamos el set de datos de prueba(testing data set) 
#creamos un nuevo array que contenga los valores escalados 
test_data = scaled_data[training_data_len - 60:, : ]

#creamos el data set x_test y y_test
x_test=[]
y_test = dataset[training_data_len: , :]

for i in range(60,len(test_data)):
  x_test.append(test_data[i-60:i, 0])


#convertir los datos en un array de numpy
x_test = np.array(x_test)


#Redimensionamos el modelo de 2d -> 3d
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1) )


#obtener los modelos que predicen los valors 
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)


#obtenemos la error cuadratico medio (RMSE)
rmse = np.sqrt(np.mean(predictions - y_test)**2 )



#graficar  los datos 
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions']=predictions
#mostrr los datos 
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('close price usd', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close','Predictions']])
plt.legend(['Train','Val','Prediction'], loc = 'lower right')
plt.show()




