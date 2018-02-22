
##################################
#
#  Physics 242
#  Lab 1
#  Problem 86
#  Group 4
#  Driver: Cameron Kimber
#  Navigator: Cameron Klotz
#  31 January 2018
#
##################################

from __future__ import division, print_function 
from visual import *
from visual.graph import *
from math import cos

#Graph Labels#
#################################
graph1 = gdisplay(title = "Torque and Kinetic Energy",
                  xtitle = "Time (seconds)",
                  x = 0, y = 400, width = 400, height = 400)
label(display = graph1.display,
      pos = vector(2.5, 2.9),
      text = 'Torque (m N)',
      color = color.cyan)
label(display = graph1.display,
      pos = vector(2.5, .6),
      text = 'Rotational Kinetic \n      Energy (J)',
      color = color.yellow)

#Constants#
##################################
M     = 2
Lrod  = 1
R     = 0.1
Laxle = 4 * R
I     = (1/12) * M  * Lrod ** 2 + (1/4) * M * R ** 2

#Objects#
##################################
rod = cylinder(pos     = vector(-1,0,0),
               radius  = R, 
               color   = color.orange,
               axis    = vector(Lrod, 0, 0))

axle = cylinder(pos    = vector(-1 + Lrod/2, 0 , -Laxle/2),
                radius = R/6,
                color  = color.red,
                axis   = vector(0, 0, 4*R))


#Parameters#
##################################
L      = vector(0, 0, 0) # angular momentum
deltat = 0.0001
t      = 0
theta  = 0
dtheta = 0

rke_graph  = gcurve(gdisplay = graph1, color = color.yellow)
torque_graph = gcurve(gdisplay = graph1, color = color.cyan)

rke = 0

#Loop#
##################################
while t < 2:
    rate(5000)
    torque = vector(0, 0, 3 * math.cos(5*t)) # constant torque

    # Apply angular momentum principle
    L = L + torque * deltat

    # Update angle and rod position
    omega = L / I
    omega_scalar = dot(omega, norm(axle.axis))
    dtheta = omega_scalar * deltat
    rod.rotate(angle = dtheta, axis = axle.axis, origin = axle.pos)
    theta += dtheta
    
    # Update kinetic energy
    rke = 1/2 * I * omega_scalar**2
    
    # Update Graph
    rke_graph.plot(pos = (t, rke))
    torque_graph.plot(pos = (t, mag(torque)))
 
    # Update time
    t = t + deltat

    
#Questions#
##################################
# D. No, in this case, the torque and kinetic energy are somehow inversely related.
