############################################
#Driver:Cameron Klotz
#Navigator:Cameron Kimber
#Physics 242L: Lab II
#February 7, 2018
############################################

from __future__ import division, print_function
from visual import *
from visual.graph import *

############################################
#Q3. Read and plot Pendulum
############################################

# Make arrays and graphs
############################################
t, thetadeg, omega = loadtxt('./phys_pend2.txt',
                            skiprows = 1,
                            unpack = True)


theta = copy(thetadeg) * pi / 180 #  I just want to say I was pulling my hair out
                                  #  before I realized theta was in degrees. -C.Kimber

fd = zeros(len(t))

G=gdisplay(title ="Numerical Derivative vs. Omega",
           x = 0, y = 400,
           width = 800, height = 800,
           ytitle = "d theta / dt (rad/s)",
           xtitle = 'time (s)')

G1  = gcurve(gdisplay=G,color=color.white)
G2  = gdots(gdisplay=G,color=color.red)

label(display = G.display, pos = vector(10, 10), text = "Numerical Derivative", color = color.red)
label(display = G.display, pos = vector(10, 5), text = "Analytical Derivative", color = color.white)

# Good ol' fashion loop
############################################
i  = 0

while i <=len(t)-1:
    rate(50)

    # Center difference cause we ain't scrubs
    if i == 0:
        fd[i] = (theta[i+1] - theta[i])/(t[i+1]-t[i])
        
    elif i == len(t) - 1:
        fd[i] = (theta[i] - theta[i-1])/(t[i]-t[i-1])
        
    else:
        fd[i] = (theta[i+1] - theta[i-1])/(t[i+1] - t[i-1])
    

    G1.plot(pos = (t[i], omega[i]))
    G2.plot(pos = (t[i], fd[i]))
    i+=1
