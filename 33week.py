from pylab import *
from scipy import special
import numpy as np
import math
from scipy.integrate import quad
def cocas(x):
    return cos(cos(x))
def exp(x):
    return vectorize(math.exp)(x)
def bne(x,n):
    return (e**x)*sin(n*x)
def bnc(x,n):
    return (cocas(x))*sin(n*x)
def ane(x,n):
    return (e**x)*cos(n*x)
def anc(x,n):
    return (cocas(x))*cos(n*x) 
x = linspace(0,2*pi,401)
x=x[:-1]
y = exp(x)
A=zeros((400,51)) 
A[:,0]=1
for k in range(1,26):
    A[:,2*k-1]=cos(k*x) 
    A[:,2*k]=sin(k*x)
a0,err = quad(exp,0,2*pi)
a0 = a0/(2*pi)
acoeff = []
acoeff.append(a0)
b0,err = quad(cocas,0,2*pi)
bcoeff = []
bcoeff.append(b0/(2*pi))
for i in range(1,26):
    a0,err = quad(ane,0,2*pi,args=(i))
    a0 = a0/pi
    acoeff.append(a0)
    a0,err = quad(bne,0,2*pi,args=(i))
    a0 = a0/pi
    acoeff.append(a0)
    b0,err = quad(anc,0,2*pi,args=(i))
    bcoeff.append(b0/pi)
    b0,err = quad(bnc,0,2*pi,args=(i))
    bcoeff.append(b0/pi)
b1 = dot(A,acoeff)
c = lstsq(A,y)[0]
i = range(51)
print(A[399,:])
print(A[:,50])
plot(i,c,"go")
title("plot of least square")
grid()
show()
plot(i,acoeff,"go")
title("error in the coeffients")
grid()
show()
plot(i,c-acoeff,"go")
title("error in the coeffients")
show()
print(acoeff)
semilogy(x,abs(b1),'ro')
semilogy(x,y,"b")
legend(("fourier series","actual curve"))
title("fourier series")
grid()
show()
b = dot(A,c)
semilogy(x,b,"ro")
semilogy(x,y,"b")
legend(("best fit","actual curve"))
title("plot by least square coeff.")
grid()
show()
semilogy(x,abs(b-y))
title("error in best fit")
grid()
show()
y = cocas(x)
b = dot(A,bcoeff)
c = lstsq(A,y)[0]
i = range(51)
plot(i,c,"go")
title("plot of least square coeff")
grid()
show()
semilogy(x,b,"r.")
semilogy(x,y,"b")
legend(("fourier series","actual curve"))
title("fourier series")
grid()
show()
b = dot(A,c)
semilogy(x,b,"ro")
semilogy(x,y,"b")
legend(("best fit","actual curve"))
title("plot by least square coeff.")
grid()
show()
semilogy(x,abs(b-y))
title("error in best fit")
grid()
show()

