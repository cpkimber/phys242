
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
graph1 = gdisplay(title = "Angle and Angular Momentum",
                  xtitle = "Time (seconds)",
                  ytitle = "Angle (Radians)",
                  x = 0, y = 400, width = 400, height = 400)
label(display = graph1.display,
      pos = vector(1.8, 10),
      text = 'Theta (rad)',
      color = color.green)


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

theta_graph  = gcurve(gdisplay = graph1, color = color.green, dot = True)


#Graph Labels#
#################################
label(display = graph1.display, pos = vector(1.8, 10),  text = 'Theta (rad)', color = color.green)



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

    # Update Graph
    theta_graph.plot(pos = (t, theta))
 
    # Update time
    t = t + deltat

print("By our best estimate, the period is 1.26, while theoretically it should be %.3f" %(2*pi/5))
#Questions#
##################################
# Theta = 0 at 1.26 sec
# It should equal zero at 2pi/5, so it does make sense


