from __future__ import division
from visual import *
from visual.graph import *  # graphing features

#Simulation of Felix Bautmgartner

#time
t = 0
dt = 0.01

#modeling felix as a ball
h = 38969.4
felix =  sphere(pos =(0,h,0), radius = 0.6, color = color.orange)
felix.mass = 110 # mass with all the equipment

#air Resitance Stuff
C = 0.5
A = 0.6 # area of the bottom of felix f
f_air = vector(0,0,0)

#gravity
r_earth= 6.371E6
G = 6.67E-11
m_earth = 5.972E24
r = r_earth + h
f_gravity = felix.mass*((G*m_earth)/(r**2) - (2*G*m_earth)/(r**3))*vector(0,-1,0) #Taylor apporximation


#total force
f_total = f_air + f_gravity



trajectory = gdisplay(title = 'height vs time',
                      xtitle = 'time', ytitle = 'speed',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)

speed_vs_time = gdisplay(title = 'speed vs time',
                      xtitle = 'time', ytitle = 'speed',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)

speed_vs_height = gdisplay(title = 'Vertical Speed vs height',
                      xtitle = 'height', ytitle = 'vertical speed',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)

height_time = gdots(gdisplay = trajectory, color = color.blue)
speed_time = gdots(gdisplay = speed_vs_time , color = color.blue)
speed_height =  gdots(gdisplay = speed_vs_height, color = color.blue)



initial_velocity = vector(0,0,0)
felix.mom =  felix.mass*initial_velocity


#loop
while felix.pos.y > 0:

    #Force of air
    rho = 1.225 * exp(-felix.pos.y/7800)
    f_air= -0.5*C*A*rho*mag2(felix.mom/felix.mass)*norm(felix.mom)
    #Force of gravity
    r = r_earth+ felix.pos.y
    f_gravity = felix.mass*((G*m_earth)/(r**2) - (2*G*m_earth)/(r**3))*vector(0,-1,0)
    #Net force
    f_total = f_air + f_gravity
    #position update
    felix.pos = felix.pos + (felix.mom/felix.mass)*dt
    #momentum update
    felix.mom = felix.mom + f_total*dt

    #plot
    height_time.plot(pos =(t,felix.pos.y))
    speed_time.plot(pos =(t,mag(felix.mom)/felix.mass))
    speed_height.plot(pos =(felix.pos.y,mag(felix.mom)/felix.mass))

    if -f_air == f_gravity:
        print(felix.mom/felix.mass)
    #increment time step
    t+= dt
