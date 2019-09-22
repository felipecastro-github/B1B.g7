import numpy as np
from math import pi
"""class calculadorabasica:
	def __init__(self, x1, y1):
		self.x = x1
		self.y = y1
	def suma(self):
		return self.x+self.y
	def resta(self):
		return self.x-self.y
	def division(self):
		if (self.y==0):
			print('No se puede dividir por cero')
		else:
			return self.x/self.y
	def multiplicacion(self):
		return self.x*self.y"""
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
	def cos (self,x):
		return np.cos(x)
	def sin (self, x):
		return np.sin(x)
	def exp (self, x):
		return np.exp(x)
				


