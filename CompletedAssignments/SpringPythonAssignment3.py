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
dt = 0.005


#Forces
Initial_F_spring = -k*x


#Window for the x position vs time
x_position = gdisplay( title = 'X- Position Vs Time',   
                       xtitle = 'time(s)', ytitle = 'x position (m)',
                       x=0, y=0,
                       width = 1000, height = 500,
                       foreground = color.black,
                       background = color.white)

#graphics curve for x position vs time
x_pos_vs_time_numerical = gdots(gdisplay = x_position, color = color.black)
x_pos_vs_time_analytical = gdots(gdisplay = x_position, color = color.red)

#loop variables
initial_velocity = vector(1,0,0)
initial_position = vector(0.6,0,0)

position = initial_position
momentum = m*initial_velocity
F_spring = Initial_F_spring
displacement = x

while t < 5:
    rate(1000)



    #Update Spring Force
    F_spring = -k*(mag(position)-L_0)*norm(position)
    print(mag(position)-L_0)

    
    #momentum update
    momentum = momentum + F_spring*dt
    #position update
    position = position + (momentum/m)*dt
    #pos_anal = 0.1*cos(sqrt(30)*t) + 0.5                    # base case
    #pos_anal = 0.1*cos(sqrt(120)*t) + 0.5                   #k = 600
    #pos_anal = (-1/sqrt(30))*cos(sqrt(30)*t - (pi/2)) + 0.5   #when V0 = 1 & r0 = 0.5#
    #pos_anal = (1/(sin(atan(-10))*(-sqrt(30))-0.4)*cos(sqrt(30)*t + atan(-10)+0.46)) + 0.5  #when V0 = 1 & r0 = 0.6#
    pos_anal = (0.208166599)*cos(sqrt(30)*t - 1.06703314)+ 0.5
    x_pos_vs_time_analytical.plot(pos = (t,pos_anal))
    x_pos_vs_time_numerical.plot(pos = (t,position.x))
    


    t+= dt


