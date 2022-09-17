#cerebro
#importamos libreria 
#problema de clasificacion binaria 


import numpy as np 
import scipy as sc 
import matplotlib.pyplot as plt

from sklearn.datasets import make_circles  

n = 500 #numero de registros de nuestros datos 
p = 2  #caracteristicas de nuestros datos 

x,y  = make_circles(n_samples = n, factor = 0.5, noise=0.05  )

plt.scatter(x[y==0 ,0], x[y==0,1] ,c='skyblue')
plt.scatter(x[y==1, 0], x[y==1,1] ,c='salmon')
plt.axis('equal')
plt.show()

#objetivo: que la red separe en  dos nuves de puntos
#clase de la capa de la red  
class neural_layer():
	def __init__(self, n_conn, n_neur, act_f):
		self.act_f = act_f
		self.b = np.random.rand(1, n_neur)*2 -1
		self.w = np.random.rand(n_conn, n_neur)*2 -1

#creamos las funciones de activacion 
sigm = (lambda x: 1/(1+np.e**(-x)),
		lambda x: x * (1-x)) 

_x= np.linspace(-5,5,100)
#plt.plot(_x,sigm[1](_x))	
#plt.show()		


#cramos las capasa de la red

#topology = [p, 4, 8, 16, 8, 4, 1]

def create_nn(topology, act_f):
  nn = []
  for l, layer in enumerate(topology[:-1]):
    nn.append(neural_layer(topology[l], topology[l+1], act_f))
  return nn

topology = [p,4,8,6,8,4,1]

neural_net= create_nn(topology, sigm)


#funcion de entrenamiento
#forward passs
#backwardpass
#gradient descent


l2_cost =  (lambda Yp, Yr:np.mean((Yp - Yr)**2),
			lambda Yp, Yr:(Yp - Yr))

#ratio de aprendizaje 


def train(neural_net, x, y, l2_cost, lr = 0.5):

	#forwardpass

	out = [(None, x)]

	for l, layer  in enumerate(neural_net): 
		z = out[-1][1] @ neural_net[0].w + neural_net[0].b
		a = neural_net[l].act_f[0](z)

	out.append((z,a))

print(out[-1][1])

train(neural_net, x, y, l2_cost, 0.5 )


import time
from IPython.display import clear_output

neural_n = create_nn(topology, sigm)

loss = []

for i in range(1000):
  #entrenamos la re 
  pY = train(neural_n, X, Y, l2_cost, lr=0.001)

  if i % 25 == 0:

     loss.append(l2_cost[0](pY, Y))

     res = 50  
    
     _x0 = np.linspace(-1.5, 1.5, res)
     _x1 = np.linspace(-1.5, 1.5, res)

     _Y = np.zeros((res, res)) 

     for i0, x0 in enumerate(_x0):
        for i1, x1 in enumerate(_x1):
          _Y[i0, i1] = train(neural_n, np.array([[x0, x1]]), Y, l2_cost, train=False)[0][0]
    
     plt.pcolormesh(_x0, _x1, _Y, cmap="coolwarm")
     plt.axis("equal")

     plt.scatter(X[Y[:, 0] == 0, 0], X[Y[:,0] == 0, 1], c="skyblue")
     plt.scatter(X[Y[:, 0] == 1, 0], X[Y[:,0] == 1, 1], c="salmon")

     clear_output(wait=True)
     plt.show()
     plt.plot(range(len(loss)),loss)
     plt.show()
     time.sleep(0.5)