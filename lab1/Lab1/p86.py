
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
graph1 = gdisplay(title = "Angle and Angular Momentum",
                  xtitle = "Time (seconds)",
                  ytitle = "Angle (Radians)",
                  x = 0, y = 400, width = 400, height = 400)

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

axle = cylinder(pos    = vector(-1/2 + Lrod/2, 0 , -Laxle/2),
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
omega_graph  = gcurve(gdisplay = graph1, color = color.red, dot = True)

#Graph Labels#
#################################
label(display = graph1.display, pos = vector(1.8, 10),  text = 'Theta (rad)', color = color.green)
label(display = graph1.display, pos = vector(.6, 14.5),  text = 'Omega (rad/s)', color = color.red)


#Loop#
##################################
while t < 2:
    rate(5000)
    torque = vector(0, 0, 2) # constant torque

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
    omega_graph.plot(pos = (t, mag(omega)))   
    # Update time
    t = t + deltat

print("The final angle theta is %.2f, and the final angular velocity is %.2f" % (theta, mag(omega)))

#Questions#
##################################
# A - Fixed the code; integrated torque/moment of inertia dt between 0 and 2 to find
# omega and theta.
#
# B - Graphing
#
#
#
#
#
#
#
#


