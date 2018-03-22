from pylab import *
import sys
if (len(sys.argv) == 6):
    n = int(sys.argv[1])
    M = int(sys.argv[2])
    p = int(sys.argv[3])
    nk = int(sys.argv[4])
    uo = int(sys.argv[5])
else:
    n = 100 #the grid Size
    p= .5   # defining the probavility at which the elctron loses its enrgy by striking the atoms of a tubelight
    M= 10   # number of electrons injected per turn.
    nk=500  # number of turns to simulate.
    u0=7    #thresh hold for the velocity
xx = zeros((M*nk))
Dx = zeros((M*nk))
u = zeros((M*nk))
I = [] #intensity of the  points where the elctrons strikes
X = [] #position of all the points after all iterations
V = [] #velocties of all the points
for k in range(nk):
    ii = where(xx >0)[0] # finding the elctrons in the tube light
    Dx[ii] = u[ii] +.5  #changing the  paramters
    xx[ii] = xx[ii] + Dx[ii] 
    u[ii] = u[ii] + 1
    pp = where(xx>=n)[0] # for all the elctrons that reach the end to be brought back to the cathode
    xx[pp] = 0
    u[pp]=0
    jj = where(u>=u0)[0]  #tracking the elements 
    ll = where(rand(len(jj))<=p)[0] #making the elemts colllide with atoms with due respect to probility
    jl = jj[ll]
    u[jl] = 0
    xx[jl] = xx[jl] - rand(len(jl))*Dx[jl] #checking for the positions of the colliding the electroms
    I.extend(xx[jl].tolist()) # updating the intensity vector
    m = (abs(normal(2,M))//1) # calculating the no. of electrons to be injected
    zz = where(xx ==0)[0] # finding empty spaces 
    zm = zz[0:int(m)]     # choosing the empty spaces where the electrons to be filled
    xx[zm] = 1 
    X.extend(xx[ii].tolist()) # updating the psotions of the electrons 
    V.extend(u[ii].tolist()) # updtaing the velocties of the elctron
hist(X, normed = True , bins = 100);xlabel("x");ylabel("X");show()
hist(V, normed = True, bins = 100);xlabel("x");ylabel("V");show()
plot(X[10000:],V[10000:],"r.");xlabel("X");ylabel("V");show()
popu,bins,listr = hist(I, normed = False , bins = 100, color = "orange");xlabel("X");ylabel("I");show()
xpos= .5*(bins[0:-1]+bins[1:])
for i in range(len(popu)):
    print xpos[i],popu[i]