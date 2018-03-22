from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
#from scipy.special import arctan
y=[]
def function(x):
    p = 1+ x*x
    y = 1/p
    return y;
def taninver(x):
	z = quad(function,0,x)
	return z[0]
x = arange(0,10,.1)
z = np.arctan(x)
for k in x:
	y.append(taninver(k))
ax = plt.subplots()
plot(x,z,'b-')
plot(x,y,'ro')
legend(("arctan","quad function"))
show()
semilogy(x,abs(y-z),'ro')
err = (y-z)
for j in err:
	print(abs(j))
title("error in $1/(1+t^{2})$")
show()
