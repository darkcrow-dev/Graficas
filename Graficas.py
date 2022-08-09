"""Graficar en python 2 variables"""

from tkinter import END
import numpy as np      #Libreria numpy
import matplotlib.pyplot as plt     #Libreria para graficar

n = 0       
m = 0
x1 = []     #Variable 1
x2 = []     #Variable 2

for i in range(0, 20):
    n = i + n/2
    x1.append(n)

for i in range(0, 15):
    m = i + 2*(m/3)
    x2.append(m)


plt.plot(x1)    #Grafica de la variable x2
plt.plot(x2, marker = 'o', linewidth = 2) #Grafina de la variable x2 con un linea gruesa
plt.grid()      #Se agregan cuadriculas
plt.xlabel('x', fontsize = 14)     #Titulo de las x   
plt.ylabel('y      ', rotation = 0, fontsize = 14)     #Titulo de las y
plt.title('2 variables')    #Titulo de la grafica
plt.show()      #Se muestran las graficas