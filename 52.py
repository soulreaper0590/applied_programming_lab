from pylab import *
import mpl_toolkits.mplot3d.axes3d as p3
Nx = 25
Ny = 25
phi = zeros((Nx,Ny))
radius = .35# so that it covers mostr of the plate but no all of it
Niter = 1500
#making phi as it was 
x = linspace(-.5,.5,Nx)
y = linspace(-.5,.5,Ny)
Y,X = meshgrid(y,x)
ii = where(Y*Y+X*X<.35*.35)
phi[ii]=1.0
contour(x,y,phi)
plot (x[ii[0]],y[ii[1]],'ro')
title('contour plot of phi')
xlabel('x');
ylabel('y')
grid();
show()
errors = zeros((Niter))
rot = []
t = [] 
for k in range(Niter):
    oldphi = phi.copy()
    phi[1:-1,1:-1] = 0.25*(oldphi[1:-1,0:-2]+oldphi[1:-1,2:]+oldphi[2:,1:-1]+oldphi[0:-2,1:-1])
    phi[0:,0]=phi[0:,1]
    phi[0:,-1]=phi[0:,-2]
    phi[0,0:]=phi[1,0:]
    #phi[-1,1:]=phi[-2,1:]
    phi[ii]=1.0
    #print phi
    errors[k] = abs(phi-oldphi).max()
    if k%50==0:
        t.append(k)
        rot.append(log(errors[k]))
her = contour(x,y,phi)
plt.clabel(her, inline=1, fontsize=10)
plot (x[ii[0]],y[ii[1]],'ro')
title('contour plot of phi')
xlabel('x'); 
ylabel('y')
grid();
show()
show()
o = range(Niter)
error = log(errors)
fx = zeros((Niter,2))
for k in range(Niter):
    fx[k:,0] = k
    fx[k:,1] = 1
A,B = lstsq(fx,error)[0]
A2,B2 = lstsq(fx[500:,0:],error[500:])[0]
print A,B
print A2,B2
yi = zeros((Niter))
yi2 = zeros((Niter))
for k in o:
    yi[k] = A*k + B
    yi2[k] = A2*k + B2
    #print y[k]
#print k
plot(o,error,'r-')
plot(o,yi2,'b-')
plot(o,yi,'g-')
title("semi log plot of error and best fits")
legend(("errors","best fit after 500","best fit from start"),loc="best")
grid()
show()
fig1=figure(4)# open a new figure
ax=p3.Axes3D(fig1)
title("The 3-D surface plot of the potential")
#print phi.T
surf = ax.plot_surface(X,Y, phi.T, rstride=1, cstride=1, cmap=cm.jet)
show()
Jx = zeros((Nx,Ny))
Jy = zeros((Nx,Ny))
Jx[1:-1,1:-1] = -.5*(phi[1:-1,0:-2]-phi[1:-1,2:]) 
Jy[1:-1,1:-1] = -.5*(phi[0:-2,1:-1]-phi[2:,1:-1])
quiver(x,y,Jx[::-1,:],Jy[::-1,:],scale = 8)
plot (x[ii[0]],y[ii[1]],'ro')
title('Vector Plot of Current')
xlabel('x');
ylabel('y')
grid(); 
show()
pro = zeros((25,25))
for k in range(25):
    for i in range(25):
        pro[k][i] = Jx[i][k]*Jx[i][k]+Jy[k][i]*Jy[k][i]+300
fig1=figure(4)# open a new figure
ax=p3.Axes3D(fig1)
title("The 3-D surface plot of the potential")
#print phi.T
surf = ax.plot_surface(X,Y, pro.T, rstride=1, cstride=1, cmap=cm.jet)
show()