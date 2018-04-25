import math
from pylab import *
from scipy import special as spc
import numpy as np
def bessel(x,v):
    y = []
    for i in x:
        y.append(1.414*((math.pi*i)**(-0.5))*cos(i-(v*math.pi/2)-(math.pi/4)))
    return y 
def calcnu(x,xo,eps,model):
    xi = []
    A = 0
    B = 0
    jj = where(x>i)
    xi = x[jj]
    # xi.append(j)
    jxi = spc.jv(1,xi) + eps
    fxi = zeros((len(xi),2))
    fx2 = zeros((len(xi),2))
    if(model=='b'):
        #model b shoul be printed
        fxi[:,0] = cos(xi)
        fxi[:,1] = sin(xi)
        A,B = lstsq(fxi,jxi)[0]
    if(model=='c'):
        #model c should be coded here
        fx2[:,0] = cos(xi)*(xi**-0.5)
        fx2[:,1] = sin(xi)*(xi**-0.5)
        A,B = lstsq(fx2,jxi)[0]
    #A,B = lstsq(fxi,jxi)[0]
    phi = arctan(-A/B)
    nu = 2.0/pi*(phi+pi/4)
    return nu 
x = linspace(0.5,20.5,41)
y = bessel(x,1)
plot (x,y)
xlabel("x")
ylabel("bessel funtion as per defunition")
show()
xo = arange(0.5,18,.5)
arrayA = []
arrayB = []
arraynu = []
arraynu1 = []
arraynu2 = []
for i in xo:
    xi = []
    jj = where(x>i)[0]
    xi = x[jj]
    print (len(xi))
    fxi = zeros((len(xi),2))
    fxi[:,0] = cos(xi)
    fxi[:,1] = sin(xi)
    fx2 = zeros((2,len(xi)))
    fx2[0,:] = cos(xi)*(xi**-.5)
    fx2[1,:] = sin(xi)*(xi**-.5)
    fx2 = fx2.transpose()
    print fx2
    jxi = spc.jv(1,xi)
    A,B = lstsq(fxi,jxi)[0]
    phi = arctan(-A/B)
    nu = 2.0/pi*(phi+pi/4)
    arraynu.append(nu)
    jxi = spc.jv(1,xi)
    A,B = lstsq(fx2,jxi)[0]
    phi = arctan(-A/B)
    nu = 2.0/pi*(phi+pi/4)
    eps = 0;
    arraynu1.append(calcnu(x,i,eps,'c'))
    eps = 0.03;
    arraynu2.append(calcnu(x,i,eps*np.random.randn(len(xi)),'c'))
#print len( arraynu)0  handles=['green dot','blue dot','red dot']
plot(xo,arraynu,'g.')
plot(xo,arraynu1,'b.')
plot(xo,arraynu2,'r.' )
legend(("eps=0 part b ",'eps=0 part c','eps = .03 part c'),loc = 'best')
ylabel(r"$\nu$")
xlabel("xo")
#legend("eps=0",'eps*rand(10)')
#plot(xo,yi)
grid()
show()
