
from __future__ import division
from visual import *
from visual.graph import * # graphing features

#Simulation of Bob Beamon world record long jump

#time
t = 0
dt = 0.01

#Modeling Beamon as a ball
bob = sphere (pos =(0,0,0), radius = 0.6, color = color.orange)
bob.mass = 80                   #Bob Beamon is 70kg according to wikipedia

#graphics

trajectory = gdisplay(title = 'Y position vs X position',
                      xtitle = 'x position (m)', ytitle = 'y position (m)',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)     

y_pos_vs_x_pos_bob = gdots(gdisplay = trajectory, color = color.blue)  

#initial conditions 
bob.pos = (0,0,0)
theta = 42*(pi/180)
take_off_velocity = 8.98
initial_velocity = take_off_velocity*vector(cos(theta), sin(theta), 0)
bob.mom =  bob.mass*initial_velocity

#Air Resistance Stuff
h= 2240                       #altitude of new mexico
C = 0.9
rho = 1.225 * exp(-h/7800)
A = 0.5
f_air = vector(0,0,0)

#gravity
r_earth= 6.371E6
G = 6.67E-11
m_earth = 5.972E24
r = r_earth + h
f_gravity = bob.mass*((G*m_earth)/(r**2) - (2*G*m_earth)/(r**3))*vector(0,-1,0) #Taylor apporximation

print(bob.mom/bob.mass)

#total force
f_total = f_air + f_gravity



while(bob.pos.y > -0.0000001):
    rate(100)

    #Force of air
    f_air= -0.5*C*A*rho*mag2(bob.mom/bob.mass)*norm(bob.mom)
    #Force of gravity
    r = r_earth+ bob.pos.y
    f_gravity = bob.mass*((G*m_earth)/(r**2) - (2*G*m_earth)/(r**3))*vector(0,-1,0)
    #Net force
    f_total = f_air + f_gravity

    #position update
    bob.pos = bob.pos + (bob.mom/bob.mass)*dt
    #momentum update
    bob.mom = bob.mom + f_total*dt
    if bob.pos.y <-0.0000001:
        print(bob.pos.x)

    #plot
    y_pos_vs_x_pos_bob.plot(pos = (bob.pos.x, bob.pos.y))
                        
    #increment time step
    t += dt 
