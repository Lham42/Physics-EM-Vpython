from __future__ import division
from visual import *
from visual.graph import * # graphing features

# simulation of a basketball free throw


# time
time = 0
dt = 0.01

# information about the ball
mass = 0.5                   # mass of basketball in kg
g = vector(0, -9.8,0)        # acceleration due to gravity
force_g = mass*g                   # Force due to gravity


height = 1.8

#Air resistance
rho = 1.22           # density of air kg/m**3
A = pi*(0.2286/2)**2    # frontal area of basketball
C = .5               # Coefficient of drag
force_air = vector(0,0,0)
total_force_air = vector(0,0,0)




# create ball and court
basketball1 = sphere(pos=(7.175/2 - 4.3,height,0), radius = 0.2286 , color = color.orange)            # makes a basketball 1
basketball2 = sphere(pos=(7.175/2 - 4.3,height,0), radius = 0.2286 , color = color.orange)            # makes a basketball 2
basketball3 = sphere(pos=(7.175/2 - 4.3,height,0), radius = 0.2286 , color = color.orange)            # makes a basketball 3
basketball4 = sphere(pos=(7.175/2 - 4.3,height,0), radius = 0.2286 , color = color.orange)            # makes a basketball 4

court = box(pos=(0, 0, 0), size=(7.175+1, 0.1,  15.2) , color=color.white)            # makes quarter of a basketball court
pole = cylinder(pos=(3.5875+0.2286+0.05,0,0), axis = (0,1,0), length = 3, radius = 0.1, color=color.white)                                  # makes pole of net
rim = ring(pos=(3.5875,3,0), axis=(0,1,0), radius=0.2286, thickness=0.05, color=color.red)
backboard = box(pos=(3.5875+0.2286+0.05, 3+0.419,0), size=(0.1,0.838,1.372), color=color.white)

#graphics

trajectory = gdisplay(title = 'Y position vs X position',
                      xtitle = 'x position (m)', ytitle = 'y position (m)',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)                         #window for y position vs x position

y_pos_vs_x_pos_no_air_ball1 = gdots(gdisplay = trajectory, color = color.blue)        # a graphics curve for y position vs x position without air drag
y_pos_vs_x_pos_no_air_ball2 = gdots(gdisplay = trajectory, color = color.red)        # a graphics curve for y position vs x position
y_pos_vs_x_pos_air_ball3 = gdots(gdisplay = trajectory, color = color.green)        # a graphics curve for y position vs x position without air drag
y_pos_vs_x_pos_air_ball4 = gdots(gdisplay = trajectory, color = color.yellow)        # a graphics curve for y position vs x position without air drag
     # a graphics curve for y position vs x position with airdrag


#loop variables
# initial velocities 1(4.2669,6,0) and 2(2.2371,10,0)
basketball1.mom = vector(4.42669*mass,6*mass,0) 
basketball2.mom = vector(2.2371*mass,10*mass,0) 
basketball3.mom = vector(4.42669*mass,6*mass,0) 
basketball4.mom = vector(2.2371*mass,10*mass,0) 

#main loop
while(basketball1.pos.y > court.pos.y or basketball2.pos.y > court.pos.y or basketball3.pos.y > court.pos.y or basketball4.pos.y > court.pos.y ):

    basketball1.pos = basketball1.pos + (basketball1.mom/mass)*dt                #position update
    basketball1.mom = basketball1.mom + (force_g)*dt

    basketball2.pos = basketball2.pos + (basketball2.mom/mass)*dt                #position update
    basketball2.mom = basketball2.mom + (force_g)*dt

    #balls with air resistance
    force_air_1= -0.5*C*A*rho*mag2(basketball3.mom/mass)*norm(basketball3.mom)
    force_air_2= -0.5*C*A*rho*mag2(basketball4.mom/mass)*norm(basketball4.mom)
    total_force_1=  force_g + force_air_1
    total_force_2=  force_g + force_air_2
    
    basketball3.pos = basketball3.pos + (basketball3.mom/mass)*dt                #position update
    basketball3.mom = basketball3.mom + (total_force_1)*dt

    basketball4.pos = basketball4.pos + (basketball4.mom/mass)*dt                #position update
    basketball4.mom = basketball4.mom + (total_force_2)*dt
    

    rate(50)
    if(basketball1.pos.y > court.pos.y):
        y_pos_vs_x_pos_no_air_ball1.plot(pos = ((basketball1.pos.x -(7.175/2 - 4.3)), basketball1.pos.y))
    if(basketball2.pos.y > court.pos.y):
        y_pos_vs_x_pos_no_air_ball2.plot(pos = ((basketball2.pos.x -(7.175/2 - 4.3)), basketball2.pos.y))
    if(basketball3.pos.y > court.pos.y):
        y_pos_vs_x_pos_air_ball3.plot(pos = ((basketball3.pos.x -(7.175/2 - 4.3)), basketball3.pos.y))
    if(basketball4.pos.y > court.pos.y):
        y_pos_vs_x_pos_air_ball4.plot(pos = ((basketball4.pos.x -(7.175/2 - 4.3)), basketball4.pos.y))
        
    time = time + dt                                                     #increment system time
