##################################
#
#  Physics 242
#  Lab 1
#  Problem 89
#  Group 4
#  Driver: Cameron Kimber
#  Navigator: Cameron Klotz
#  31 January 2018
#
##################################

from __future__ import division, print_function 
from visual import *
from visual.graph import *

graph1 = gdisplay(title = "Theta vs. Time",
                  xtitle = "Time (seconds)",
                  ytitle = "Angle (Radians)",
                  x = 0, y = 500, width = 400, height = 400)
graph2 = gdisplay(title = "Energy",
                  xtitle = "Time (seconds)",
                  ytitle = "Energy (joules)",
                  x = 500, y = 500, width = 400, height = 400)

#Constants#
##################################
M     = 2
R     = 0.2
thick = 0.02
I     = M * R ** 2
r     = 0.9 * R
Lpeg  = 5 * thick



#Objects#
##################################
wall = box(pos = vector(-1.2 * R, 0, 0),
           size = (0.01, 2.4 * R, 0.8 * R),
           color = color.green)

disk = cylinder(pos = vector(0, 0, -thick/2),
                radius = R,
                axis = vector(0, 0, thick),
                color = color.white,
                opacity = 0.7,
                material = materials.rough)

axle = cylinder(pos = vector(0, 0, -Lpeg/2),
                radius = 0.05 * R,
                color = color.red,
                axis = vector(0, 0, Lpeg))

peg = cylinder(pos = vector(r, 0, -Lpeg/2),
               radius = 0.03 * R,
               color = color.red,
               axis = vector(0, 0, Lpeg))

#Parameters#
##################################
theta = pi/6
peg.rotate(angle = theta, axis = axle.axis, origin = axle.pos)
rspring = 0.05 * R

springF = helix(pos = vector(wall.x, r, 1.5 * thick),
                radius = 0.05 * R,
                color = color.orange,
                coils = 15,
                thickness = 0.4 * rspring)

springB = helix(pos = vector(wall.x, r, -1.5*thick),
                radius = 0.05 * R,
                color = color.orange,
                coils = 15,
                thickness = 0.4 * rspring)

end = peg.pos + vector(0, 0, Lpeg/2 + springF.pos.z)
springB.axis = springF.axis = end - springF.pos

t = 0
deltat = 0.001
dtheta = 0
ks = 1.5
L0 = 0.26
L = vector(0, 0, 0)

#Create Graphs#
#################################
theta_graph  = gcurve(gdisplay = graph1)
ke_graph     = gcurve(color = color.white,  gdisplay = graph2)
se_graph     = gcurve(color = color.orange, gdisplay = graph2)
etot_graph   = gcurve(color = color.green,  gdisplay = graph2)

#Graph Labels#
#################################
label(display = graph2.display, pos = vector(5, .21),  text = 'Kinetic Energy (J)', color = color.white)
label(display = graph2.display, pos = vector(5, .1),  text = 'Spring Energy (J)', color = color.orange)
label(display = graph2.display, pos = vector(5, .3),  text = 'Total Energy (J)', color = color.green)

##
while t < 6:
    rate(1000)
    
    # Calculate spring force F acting on peg
    deltax  = mag(springB.axis - springB.pos) - L0 
    Fmag    = 2 * ks * deltax
    Fhat    = norm(springF.pos - springF.axis)
    Fspring = Fmag * Fhat
    

    # Torque due to spring
    tnet = cross(peg.pos-axle.pos, Fspring)
    
    # Update L
    L = L + tnet * deltat
    
    # Calculate omega
    omegavec = L / I
    omega = dot(omegavec, norm(axle.axis))
    
    # Calculate dtheta and theta
    dtheta = omega * deltat
    theta += dtheta

    # Update Energy
    ke = 1/2 * I * omega**2
    se = ks * deltax ** 2
    etot = ke + se

    # Update graph
    theta_graph.plot(pos = (t, theta))
    ke_graph.plot(pos = (t, ke))
    se_graph.plot(pos = (t, se))
    etot_graph.plot(pos = (t, etot))
    
    
    # Update disk and peg positions
    disk.rotate(angle = dtheta, axis = axle.axis, origin = axle.pos)
    peg.rotate(angle = dtheta, axis = axle.axis, origin = axle.pos)
    
    # Update spring lengths:
    end = peg.pos + vector(0, 0, Lpeg/2 + springF.pos.z)
    springF.axis = end - springF.pos
    springB.axis = springF.axis

    # Update time
    t += deltat
    
#Questions#
##################################
##a) It rotates
##b) It is a harmonic oscillator
## with a period ~11.87 s    
##c) The energy is constant, as it should be.
##
