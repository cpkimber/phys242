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
#Q1. Trig file
############################################
T=arange(-90, 92, 2, dtype=None)
T2=copy(T)*2*pi/360
t=0
F=open('./trig.txt', 'w')
header1=('Theta    Sin(theta)    Cos(theta)    Sin^2(theta)+Cos^2(theta)\n')
header2=('==============================================================\n')
F.writelines(header1)
F.writelines(header2)
while (t < 91):
    c=cos((T2[t]))
    s=sin((T2[t]))
    ccss=cos((T2[t]))**2+sin((T2[t]))**2
    F.write('%3d       %7.4f       %7.4f \t%2.18f\n' %(T[t],s,c,ccss))
    t += 1
F.close()

