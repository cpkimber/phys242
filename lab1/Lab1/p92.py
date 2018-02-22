
##################################
#
#  Physics 242
#  Lab 1
#  Problem 92
#  Group 4
#  Driver: Cameron Kimber
#  Navigator: Cameron Klotz
#  6 February 2018
#
##################################

from __future__ import division, print_function 
from visual import *
from visual.graph import *
from math import cos, sin, acos
graph1 = gdisplay(title = "Angle and Angular Momentum",
                  xtitle = "Time (seconds)",
                  ytitle = "Angle (Radians)",
                  x = 50, y = 500, width = 800, height = 400)

#Constants#
##################################
M      = 2
Lrod   = 1
g      = 9.8
R      = 0.1
Laxle  = 4 * R
I      = (1/3) * M * Lrod**2
theta  = pi/2
theta  = pi - theta

#Objects#
##################################
rod = box(pos      = vector(Lrod/2*sin(theta),Lrod/2*cos(theta), 0),
          size     = (1, 0.01, 0.03),
          color    = color.yellow,
          material = materials.wood,
          axis     = vector(sin(theta), cos(theta), 0))

axle = cylinder(pos    = vector(-1/2 + Lrod/2, 0 , -Laxle/4),
                radius = R/6,
                color  = color.red,
                axis   = vector(0, 0, 2*R))

r    = (rod.axis - rod.pos)/2

#Parameters#
##################################
L      = vector(0, 0, 0) 
deltat = 0.001
t      = 0
dtheta = 0
theta_graph  = gcurve(gdisplay = graph1, color = color.green, dot = True)
omega_graph  = gcurve(gdisplay = graph1, color = color.red, dot = True)

#Graph Labels#
#################################
label(display = graph1.display, pos = vector(.25, 1),  text = '|Theta| (rad)', color = color.green)
label(display = graph1.display, pos = vector(.25, -.5),  text = 'Omega z (rad/s)', color = color.red)

#Loop#
##################################
while t < 3:
    rate(500)

    # Update force
    fhat = vector(0, -1, 0)
    fmag = M * g
    Fvec = fhat * fmag

    # Update torque
    torque = cross(r, Fvec)
    
    # Apply angular momentum principle
    L = L + torque * deltat

    # Update angle and rod position
    omega = L / I
    omega_scalar = dot(omega, norm(axle.axis))
    dtheta = omega_scalar * deltat
    rod.rotate(angle = dtheta, axis = axle.axis, origin = axle.pos)
    r     = (rod.axis - rod.pos)/2
    rhat  = r/mag(r)

    # Update Theta
    theta = acos(dot(rhat,fhat))
    
    # Update Graph
    theta_graph.plot(pos = (t, theta ))
    omega_graph.plot(pos = (t, (omega[2])))   
    # Update time
    t = t + deltat


#Questions#
##################################
# It is a harmonic oscillator,
# which is most evident at
# small angles.
# Around pi/3 and above, the small
# angle approximation begins to
# break down/ deviate by a
# considerable percentage.

small_angle_t = 2 * pi * (sqrt(I/(M * g * mag(r))))
print("The small angle approximation gives a period of %2.3f" % small_angle_t)
