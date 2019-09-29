#archivo para la funciones de una calculadoracientifica
import numpy as np
from math import *
 
class calculadora:
	def suma(self,x
	,y):
		return np.array(x)+np.array(y)
		
	def resta(self,x,y):
		return np.array(x)-np.array(y)
		
	def multiplicacion(self,x,y):
		return np.array(x)*np.array(y)
		
	def division(self,x,y):
		if (y==0):
			print('la division por cero no existe')
		else:
			return (np.array(x)*1.0/np.array(y))
		
class calculadoracientifica(calculadora):
	def media(self,x):
		return (np.sum(x)*1.0)/len(x)
	
	def mediaCuadratica (self,x):
		return self.media(np.array(x)**2)

	def varianza (self,x):
		return self.media((np.array(x)-self.media(np.array(x)))**2)

	def desviacionEstandar (self,x):
		return sqrt(self.varianza(np.array(x)))

	def  correlacion(self,x,y):
		return self.media(np.array(x)*np.array(y))
		
	def	FuncionDensidadProbabilidad(self,x):
		z=[ ]
		y=[ ]
		P=np.zeros(len(x))
		for i in range (len(x)):
			for j in range(len(x)):
				if (x[i]==x[j]):
					P[i]=P[i]+1
		for i in range (len(x)):
			if x[i] not in z :
				z.append(x[i])
				y.append(P[i]/len(x))
		t=zip(z,y)
		t.sort()
		q,w=zip(*t)
		return(list(q),list(w))
	def FuncionDistribucionAcumulativa(self,x,f):
		z=f[0][:]
		f=f[1][:]
		if x in z:
			return np.sum(f[:(z.index(x)+1)])
		else:
			print('Error: X no esta')
print('Calculadora (Operaciones: suma, resta, division, multiplicacion) \n')
x = input('ingrese el valor de x = ')
y = input('\n ingrese el valor de y = ')
a=calculadoracientifica()
print ('x + y = ' + str(a.suma(x,y)))
print ('x - y = ' + str(a.resta(x,y)))
print ('x * y = ' + str(a.multiplicacion(x,y)))
print ('x / y = ' + str(a.division(x,y)))
print ('Media de x = ' + str(a.media(x)))	
print ('Media Cuadratica de x = ' + str(a.mediaCuadratica(x)))
print ('Varianza de x = ' + str(a.varianza(x)))
print ('Desviacion estandar de x = ' + str(a.desviacionEstandar(x)))
print ('Correlacion de x = ' + str(a.correlacion(x,y)))
print ('Funcion de densidad de probabilidad de x = ' + str(a.FuncionDensidadProbabilidad(x)))
print ('Funcion de distribucion acumulativa de x = ' + str(a.FuncionDistribucionAcumulativa(x[1], a.FuncionDensidadProbabilidad(x))))
