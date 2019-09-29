#archivo para la funciones de una calculadora
import numpy as np
from math import *
 
class calculadora:
	def suma(self,x,y):
		return x+y
		
	def resta(self,x,y):
		return x-y
		
	def multiplicacion(self,x,y):
		return x*y
		
	def division(self,x,y):
		if (y==0):
			print('la division por cero no existe')
		else:
			return (x/y)
		

print('Calculadora (Operaciones: suma, resta, division, multiplicacion) \n')
x = float(input('ingrese el valor de x = '))
y = float(input('\n ingrese el valor de y = '))
a=calculadora()
print ('x + y = ' + str(a.suma(x,y)))
print ('x - y = ' + str(a.resta(x,y)))
print ('x * y = ' + str(a.multiplicacion(x,y)))
print ('x / y = ' + str(a.division(x,y)))
	

