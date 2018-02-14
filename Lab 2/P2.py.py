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
#Q2.How to Read
############################################

# Define variables/ make arrays
############################################
columnT,columns,columnc,columnccss=loadtxt('./trig.txt',skiprows=2,unpack=True)
G=gdisplay(title ="Derivative of sine vs cosine", x = 0, y = 400, width = 800, height = 800)
G1  = gcurve(gdisplay=G,color=color.blue)
G2  = gdots(gdisplay=G,color=color.red)
columnT=columnT*2*pi/360
f  = zeros(len(columnT))
fc = copy(columnc)
fd = zeros(len(columnT))
i=0

# Calculate derivate and plot
############################################
for i in range(len(columnT)):
    rate(50)
    f[i]  = sin(columnT[i])

    #Forward difference
    if i == len(columns):
        fd[i] = (f[i+1]-f[i])/(columnT[i+1]-columnT[i])
    else:
        fd[i] = (f[i]-f[i-1])/(columnT[i]-columnT[i-1])


    G1.plot( pos=(columnT[i],fc[i]))
    G2.plot( pos=(columnT[i],fd[i]))
