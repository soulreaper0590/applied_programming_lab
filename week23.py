from pylab import *
from scipy import special 
import matplotlib.patches as mpatches
import numpy as np
import matplotlib.lines as mlines
def function(x):
	return 1/(1+x*x)
def integrate(a,b):
	n = int(((b-a)/.01))
	integral = 0;
	for i in range(0,n):
		pro = 0;
		h = .01;
		starter = function(a) + function(a + i*(h))
		for k in range(1,i+1):
			pro = pro + function(a + k*(h))
		integral =  ( h*(pro - (starter)/2))
	return integral
print(integrate(0,1))
def integrate2 (a,b,h):
	x = arange(a,b,h)
	integral = h*(np.cumsum(function(x))-(function(x[0])/2)-function(x)/2)
	return integral
h=.01;
harr = [];
errorarr = [];
errorarr2 = [];
while (True):
	alpha_higher = integrate2(0,5,h)
	x = arange(0,5,h)
	alpha_lower = integrate2(0,5,h/2)
	error = [];
	error2 = [];
	n = int(1/h)
	for k in range(0,n):
		error.append(abs(alpha_lower[2*k]-alpha_higher[k]))
		error2.append(abs(alpha_higher[k]-np.arctan(x[k])))
	print(h)
	harr.append(h)
	errorarr.append(max(error))
	errorarr2.append(max(error2))
	if(abs(max(error))<=10**(-8)):
		break
	else:
		h = h/2;

loglog(harr,errorarr,"g+",label = "Estimated Error")
loglog(harr,errorarr2,"ro", label = "Exact Error")
legend(("Actual Error","Estimated Error"))
show()
