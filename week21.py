from pylab import *
def function(x):
    p = 1+ x*x
    y = 1/p
	return y
z = arange(0,5,.1)
x = function(z)
plot(z,x)
show()
