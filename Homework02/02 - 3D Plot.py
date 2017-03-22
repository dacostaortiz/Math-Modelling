import numpy as np
import pylab as pl
import os
from mpl_toolkits.mplot3d import Axes3D

path = '/data/'
data = []
for f in os.listdir(os.getcwd()+path):
    r =  np.loadtxt(os.getcwd()+path+f)
    data.append(r)

#create figure
pl.rc('font',size=10)
fig = pl.figure(figsize=(9,8),dpi=100)
ax = fig.gca(projection='3d')

#draw lines
c = ['b','g','r','c','k']
labels = ['$r=4M$','$r=5M$','$ISCO$','$r=6M$','$r=7M$']
for i, d in enumerate(data):
    ax.plot(d[:,2],d[:,3],d[:,4],c[i], label=labels[i])

#create and plot a sphere 
r   = 2
pi  = np.pi
cos = np.cos
sin = np.sin
phi,theta = np.mgrid[0.0:pi:100j,0.0:2.0*pi:100j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)
ax.plot_surface(x,y,z, rstride=1,cstride=1,color='k', alpha=0.6,linewidth=0)

#set plot limits 
ax.set_xlim3d([-8,8])
ax.set_ylim3d([-8,8])
ax.set_zlim3d([-7,7])

#labels
pl.title('Timelike geodesics in the Schwarzschild equatorial plane')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
pl.legend(loc=4,fancybox=True, shadow=True)
pl.show()
