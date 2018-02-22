
##################################
#
#  Physics 242
#  Lab 1
#  Problem 87
#  Group 4
#  Driver: Cameron Kimber
#  Navigator: Cameron Klotz
#  31 January 2018
#
##################################

from __future__ import division, print_function 
from visual import *
from math import cos

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
L      = vector(0, 0, 0) 
deltat = 0.0001
t      = 0
theta  = 0
dtheta = 0
axle.p = vector(0, 0, 0)



#Loop#
##################################
while t < 7:
    rate(5000)
    torque = vector(0, 0, 3 * math.cos(5*t)) # constant torque
    force  = vector(0.1, 0, 0)

    # Apply momentum principle
    axle.p = axle.p + force * deltat
    
    # Apply angular momentum principle
    L = L + torque * deltat

    # Update angle and rod position
    axle.pos = axle.pos + axle.p * deltat / M
    rod.pos = rod.pos + axle.p * deltat / M
    omega = L / I
    omega_scalar = dot(omega, norm(axle.axis))
    dtheta = omega_scalar * deltat
    rod.rotate(angle = dtheta, axis = axle.axis, origin = axle.pos)
    theta += dtheta

    # Update time
    t = t + deltat

#Questions#
##################################
# The rod continues swinging as the axle accelerates
# to the right.
