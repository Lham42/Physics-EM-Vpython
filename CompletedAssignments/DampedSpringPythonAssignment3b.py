from __future__ import division
from visual import *
from visual.graph import*
import math

#ignoring mass of spring and friction forces like air drag, this program finds the position of of the block a s a function of time. The initial position and velocity of the block will vary. We will then consider the a

#Information of the Spring
m = 5
k = 150 #spring constant
L_0 = 0.5 #equilibrium length

x = vector(0.1,0,0) #initial displacement

#time
t = 0
dt = 0.01

#Water resistance
rho = 997 #density of water kg/mg**3
A = 0.5   #frontal area of the mass
C = 0.75
force_water = vector(0,0,0)

#Forces
Initial_F_spring = -k*x
force_total = 0;


#Window for the x position vs time
x_position = gdisplay( title = 'X- Position Vs Time',   
                       xtitle = 'time(s)', ytitle = 'x position (m)',
                       x=0, y=0,
                       width = 1000, height = 500,
                       foreground = color.black,
                       background = color.white)

#graphics curve for x position vs time
x_pos_vs_time_numerical = gdots(gdisplay = x_position, color = color.black)
#x_pos_vs_time_analytical = gdots(gdisplay = x_position, color = color.red)

#loop variables
initial_velocity = vector(0,0,0)
initial_position = vector(0.6,0,0)

position = initial_position
momentum = m*initial_velocity
F_spring = Initial_F_spring
displacement = x
force_total = F_spring

while t < 5:
    rate(1000)



    #Update Spring Force
    F_spring = -k*(mag(position)-L_0)*norm(position)
    force_water = -0.5*C*A*rho*mag2(momentum/m)*norm(momentum)
    force_total = F_spring + force_water

    
    #momentum update
    momentum = momentum + force_total*dt
    #position update
    position = position + (momentum/m)*dt
    pos_anal = 0.1*cos(sqrt(30)*t) + 0.5                    # base case
    
    #x_pos_vs_time_analytical.plot(pos = (t,pos_anal))
    x_pos_vs_time_numerical.plot(pos = (t,position.x))
    


    t+= dt


