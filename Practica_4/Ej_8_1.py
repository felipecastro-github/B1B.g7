import numpy as np
import math
from matplotlib import pyplot as plt

def work(input_items, output_items):
    in0 = input_items[0]
    out0 = output_items[0]
    out0[:]=abs(np.fft.fftshift(np.fft.fft(in0,N)))
    return len(out0)


f=1378.
Fsamp= 8000.
N=128 
n=np.linspace(0,N-1,N)
t=n/Fsamp
in_sig=np.cos(2.*math.pi*f*t)
out_sig=np.array([0.]*N) 
 
in_sig= np.array([in_sig])
out_sig=np.array([out_sig])
 
d=work(in_sig,out_sig)
 
Fmin=-Fsamp/2.
Fresol=Fsamp/N
Fmax=-Fmin-Fresol
f=np.linspace(Fmin,Fmax,N)
plt.plot(f,out_sig[0])
plt.show()	

