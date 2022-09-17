"""# anaisis de datos
#guido Van Rossun creador de python
#no se si es necesario instalar anaconda 
---->numpy biblioteca de dados
---->scipy
---->pandas
---->scikit lern
---->matplotlib
---->seaborn
---->statsmodels   """

#precio bitcoin enero 1 2020 -> enero 1 2021  

import pandas as pd 
import matplotlib.pyplot as plt


#obtenemos el dataframe de trabajo
df_precio= pd.read_csv('BTC-USD 2019 2021.csv', header=0,names=['fecha', 'abre','high','low','close','adj_close','volumen'])


# hacemos la grafica mediante matplotlib.pyplot  
plt.figure(figsize=(20.5, 7.5))
plt.plot(df_precio['close'], label= 'btc/usd')
plt.title("HISTORIAL BTC/USD 01/01/2020 -> 01/01/2021")
plt.xlabel('fecha')
plt.ylabel('precio cierre')
plt.legend('upper right')
plt.show()





