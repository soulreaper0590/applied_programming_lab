from pylab import *
import numpy as np
import math
from scipy.integrate import quad
def cocas(x):
    return cos(cos(x))
def exp(x):
    return vectorize(math.exp)(x)
def bne(x,n):
    return exp(x)*sin(n*x)
def bnc(x,n):
    return (cocas(x))*sin(n*x)
def ane(x,n):
    return (e**x)*cos(n*x)
def anc(x,n):
    return (cocas(x))*cos(n*x)                    
a0,err = quad(exp,0,2*pi)
acoeff = []
acoeff.append(a0/(2*pi))
b0,err = quad(cocas,0,2*pi)
bcoeff = []
bcoeff.append(b0/(2*pi))
for i in range(1,26):
    a0,err = quad(ane,0,2*pi,i)
    acoeff.append(abs(a0)/pi)
    a0,err = quad(bne,0,2*pi,i)
    acoeff.append(abs(a0)/pi)
    b0,err = quad(anc,0,2*pi,i)
    bcoeff.append(abs(b0)/pi)
    b0,err = quad(bnc,0,2*pi,i)
    bcoeff.append(abs(b0)/pi)
n = arange(0,51,1)
#plot(n,bcoeff,"r-")
semilogy(n,acoeff,"ro")
xlabel("n")
ylabel("coeff of exp(x)")
grid()
show()
loglog(n,acoeff,"ro")
xlabel("n")
ylabel("coeff of exp(x)")
grid()
show()
semilogy(n,bcoeff,"ro")
xlabel("n")
ylabel("coeff of cos(cos(x))")
grid()
show()
loglog(n,bcoeff,"ro")
xlabel("n")
ylabel("coeff of cos(cos(x))")
grid()
show()
