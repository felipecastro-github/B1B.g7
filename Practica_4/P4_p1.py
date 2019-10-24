import numpy as np
import math
import matplotlib.pyplot as plt

N=8
k=1
n=np.linspace(0,N-1,N)
signal=np.cos(2.*math.pi*k*n/N)
#signal=np.cos(2.*math.pi*f*n/Fsamp)
fourier = np.fft.fft(signal)
fourier_mejor=np.fft.fftshift(fourier)

plt.plot(fourier,n)
