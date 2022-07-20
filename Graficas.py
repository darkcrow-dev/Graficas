"""Graficar en python 2 variables"""

import numpy as np      #Libreria numpy
import matplotlib.pyplot as plt     #Libreria para graficar

x = np.arange(0,10,0.2) #Rango de las x para que se visualice la grafica
y1 = np.cos(x)  #Variable 1
y2 = np.sin(x)  #Variable 2

plt.plot(x,y1,'o',linewidth=3,color=(0.2,0.1,0.4))  #La variable se vuelve en circulos
plt.plot(x,y2,'-',linewidth=2,color='g')    #La variable se vuelve verde y lineal
plt.grid()      #Agrega cuadriculado a la grafica
plt.axis('equal')
plt.xlabel('x')     #Titulo de las x
plt.ylabel('y')     #Titulo de las y
plt.title('2 variables')    #Titulo de la grafica
