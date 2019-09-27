import numpy as np
from math import pi

class calculadorabasica:
	def suma(self,x,y):
		return x+y
	def resta(self,x,y):
		return x-y
	def division(self,x,y):
		if (y==0):
			print('No se puede dividir por cero')
		else:
			return x/y
	def multiplicacion(self,x,y):
		return x*y
		
class calculadoracientifica(calculadorabasica):
	def coseno (self,x):
		return np.cos(x)
	def seno (self, x):
		return np.sin(x)
	def expo (self, x):
		return np.exp(x)
				


