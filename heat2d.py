"""2D Heat equation using finite differences"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import math
import warnings 

## ignore MatplotlibDeprecationWarning
warnings.filterwarnings("ignore",".*GUI is implemented.*")



# PHYSICAL PARAMETERS

K = 0.5     #Diffusion coefficient
Lx = 1.0    #Domain size x
Ly = 1.0    #Domain size y
Time = 0.2  #Integration time
S = 1.0     #Source term

# NUMERICAL PARAMETERS

NT = 2000            #Number of time steps
NX = 100             #Number of grid points in x
NY = 100             #Number of grid points in y
dt = Time/(NT*2)     #Grid step (time)
dx = Lx/(NX-2)       #Grid step in x (space)
dy = Ly/(NY-21)      #Grid step in y (space)


if abs(dt) > (dx*dx)/(2.0):
    print 'Warning: Instable numerical scheme->'
    print 'dt (%s) Must be less than: %s '%(dt,(dx*dx)/(2.0))
    sys.exit(1)
 

xx = np.linspace(0,Lx,NX)
yy = np.linspace(0,Ly,NY)


T = np.zeros((NX,NY))
RHS = np.zeros((NX,NY))


# Main loop
for n in range(0,NT):
   
    RHS[1:-1,1:-1] = dt*K*( (T[:-2,1:-1]-2*T[1:-1,1:-1]+T[2:,1:-1])/(dx**2)  \
                         + (T[1:-1,:-2]-2*T[1:-1,1:-1]+T[1:-1,2:])/(dy**2) )
    
    T[1:-1,1:-1] += (RHS[1:-1,1:-1]+dt*S)


# Plot every 100 time steps
    if (n%100 == 0):
       plotlabel = "t = %1.2f" %(n * dt)
       plt.pcolormesh(xx,yy,T, shading='flat')
       plt.title(plotlabel)
       plt.axis('image')
       plt.draw()
       plt.pause(0.05)


print "Iterations End!"

plt.show()

