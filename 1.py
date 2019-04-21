import numpy as np
import matplotlib.pyplot as plt
from dftfun import dft
N=int(input("enter order of dft:"))
n=int(input("enter n value:"))
k=np.arange(n)
f1=int(input("enter first wave frequency:"))
f2=int(input("enter second wave frequency:"))
fs=int(input("enter sampling frequency:"))
x1=np.sin(2*np.pi*k*f1/fs)
X1=dft(x1,N,n)
x2=np.sin(2*np.pi*k*f2/fs)
X2=dft(x2,N,n)
z=x1+x2
x3=dft(z,N,n)
X3=X1+X2
plt.subplot(211)
plt.plot(k,np.abs(x3))
plt.title("dft(x1+x2)")
plt.subplot(212)
plt.plot(k,np.abs(X3))
plt.title("X1+X2")
plt.show()
