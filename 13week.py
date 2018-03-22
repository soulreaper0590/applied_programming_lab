from pylab import *
import numpy as np
import math
def cocas(x):
    return cos(cos(x))
def exp(x):
    return e**x
x = arange(-2*pi,4*pi,.01)
y = cocas(x)
z = exp(x)
plot(x,y,"r.")
xlabel("x")
ylabel("cos(cos(x))")
grid()
show()
semilogy(x,z,"b-")
xlabel("x")
ylabel("exp(x)")
grid()
show()                     
