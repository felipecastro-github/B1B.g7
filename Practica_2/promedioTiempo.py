import numpy as np
import scipy.integrate
import random
import matplotlib.pyplot as plt

#x=input('ingrese el valor de x = ')
def promtime(x):
	"Calcula el promedio de tiempo de un vector"
	return (1.0/(len(x)-1))*scipy.integrate.simps(x)
def media(x):
		return (np.sum(x)*1.0)/len(x)
x=[ ]
for i in range(100):
	x.append(10*pow(-1,(round(random.random(),0)))*random.random())

print('El promedio de tiempo del vector x es = ' + str(promtime(x)))
print('La media del vector x es = ' + str(media(x)))
plt.plot(np.linspace(0,10,100),x)
plt.xlabel('t[s]')
plt.ylabel('Muestras[Sa]')
plt.show()




