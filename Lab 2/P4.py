############################################
#Driver:Cameron Klotz
#Navigator:Cameron Kimber
#Physics 242L: Lab II
#February 7, 2018
############################################
from __future__ import division, print_function
from visual import *
from visual.graph import *
##############################################
###Q4. P. 51 Metal rod and Meteorite
##############################################

graph = gdisplay(title = "Energies",
                 xtitle = "time (sec)",
                 ytitle = "Energy (Joules)",
                 x = 0, y = 400, width = 600, height = 600)

M=1.3
m=.06
Lrod=.4
d=Lrod/2
vi=200
vf=60
thet1=26*2*pi/360
thet2=82*2*pi/360

    #Spare the rod
rod = box       (pos      = vector(0,0,0),
                 size     = (.005,Lrod,.005), 
                 color    = color.white,
                 axis     = vector(d, 0, 0),
                 material = materials.plastic)
    #Spoil the meatyor
meatyor= sphere (pos      = vector(-cos(thet1),.2-sin(thet1),0),
                 radius   = .015,
                 color    = color.red,
                 material = materials.marble)


    #Parameters

I      =(1/12) * M * Lrod ** 2 
deltat = 0.000001
t      = 0
theta  = 0
dtheta = 0
axle   = vector(0, 0, -1)
pballi = vi * vector(cos(thet1), sin(thet1), 0) * m
pballf = vf * vector(-cos(thet2), sin(thet2), 0) * m
pball  = pballi
r      = vector(meatyor.pos - rod.pos)
Lball  = cross(r, pball)
L      = vector(0, 0, 0)
Ltot   = Lball - L
p_rod  = vector(0,0,0)

etot_graph = gdots(gdisplay = graph, color = color.white)
emet_graph = gcurve(gdisplay = graph, color = color.red)
esti_graph = gcurve(gdisplay = graph, color = color.green)

label(display = graph.display, pos = vector(8e-3,200),  text = 'KE rod', color = color.green)
label(display = graph.display, pos = vector(8e-3,300),  text = 'Total Energy', color = color.white)
label(display = graph.display, pos = vector(8e-3,100),  text = 'KE meteor', color = color.red)

while t < .0075:
    rate(2500)

    # Momentum Principle
    meatyor.pos = meatyor.pos + (pball/m)*deltat
    r = meatyor.pos - rod.pos
    
    # Ricochet
    if meatyor.pos.x > (-rod.size.x/2 - meatyor.radius):
        pball = pballf
        Lball = cross(r, pball)

    # Rotate the rod
    if pball == pballf:
        L = Ltot - Lball
        omega = L / I
        omega_scalar = mag(omega)
        dtheta = omega_scalar * deltat
        rod.rotate(angle = dtheta, axis = axle, origin = rod.pos)
        p_rod   = pballi - pballf
        rod.pos = rod.pos + (p_rod/M) * deltat
        
    kmet = mag(pball)**2/(2*m) 
    krod = mag(p_rod)**2/(2*M) + mag(L)**2/(2*I)

    etot_graph.plot(pos = (t, krod + kmet))
    emet_graph.plot(pos = (t, kmet))
    esti_graph.plot(pos = (t, krod))
    t += deltat


print("The linear velocity of the stick is", p_rod/M, "m/s.")
print("The angular velocity of the rod is %2.2f rad/s." % omega_scalar)




