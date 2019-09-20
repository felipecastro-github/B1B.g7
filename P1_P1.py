from math import *
import numpy as np
#import cmath

x=0.4
y=1.3

z=x+y
h=cos(x)
g=np.exp(2*pi*x*1j)
print('x y y escalares\n')
print ('x = '+str(x))
print ('y = '+str(y))
print ('z = x+y = '+str(z))
print ('h = cos(x) = '+str(h))
print ('g = np.exp(2*pi*x*1j) = '+str(g))
X=np.array([1,2,3,4,5])
Y=np.array([10,9,8,7,6])

Z=X+Y
H=np.cos(X)
G=np.exp(2*pi*X*1j)
print ('\nX y Y vectores \n')
print ('X = '+str(X))
print ('Y = '+str(Y))
print ('Z = X+Y = '+str(Z))
print ('H = cos(X) = '+str(H))
print ('G = np.exp(2*pi*X*1j) = '+str(G))
