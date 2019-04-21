from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x,N,k):
	j=cm.sqrt(-1)
	X=[]
	w=np.linspace(-np.pi,np.pi,N)
	for i in range(0,k):
		s=0
		for n in range(0,len(x)):
			y=np.exp(-j*2*np.pi*i*n/N)
			s=s+(x[n]*y)
		X.append(s)
	return X
