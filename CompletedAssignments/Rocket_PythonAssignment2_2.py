from __future__ import division
from visual import *
from visual.graph import * # graphing features

#simulation of a rocket

# time
time = 0
dt = 0.0001

#information about the rocket
mass = 0.5                                  #mass of rocket (close to the apogee rocket cesaroni p38-3g mellow (I55) mass)
g = vector(0,-9.8,0)                    #acceleration due to gravity
force_g = mass*g                        #gravitational force


#conditions:
thrust = False 
drag = False
loss = False

#Air resistance
rho = 1.22           # density of air kg/m**3
A = 0.01   
C = 0.2*1.25   *0.75            # Coefficient of drag

#rocket fuel loss
fuel_loss = (mass*0.6)/5



#Model rocket as a ball
rocket = sphere(pos=(0,1.85,0), radius = 0.2, color = color.orange)
ground = box(pos=(0, 0, 0), size=(10, 0.1,  15) , color=color.white)  

#graphics
trajectory = gdisplay(title = 'Y position vs X position',
                      xtitle = 'x position (m)', ytitle = 'y position (m)',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)                         #window for y position vs x position

velocity = gdisplay(title = 'Y Velocity Time',
                      xtitle = 'Y Velocity', ytitle = 'Time',
                      x=0, y=0,
                      width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)    

y_pos_vs_x_pos_rocket = gdots(gdisplay = trajectory, color = color.blue)    # a graphics curve for y position vs x position
y_vel_vs_t_rocket = gdots(gdisplay = velocity, color = color.red)

#loop variables
theta = 45*(pi/180)
rocket.vel = vector(10*cos(theta), 10*sin(theta),0)
rocket.mom = mass*rocket.vel
max_speed = mag(rocket.vel)

#main loop
while(rocket.pos.y > ground.pos.y):
    rate(1000)
    if thrust == False and drag == False and loss == False:
        rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      #position update
        rocket.mom = rocket.mom + (force_g)*dt 

    #Include thrust after 0.5 s
    if thrust == True and drag == False and loss == False:
        if (time > 0.5) and (time <5.5):
            thrust_force = 100*norm(rocket.mom)
            force_total = force_g + thrust_force
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt                              
        else:
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_g)*dt
    if thrust == True and drag == True and loss == False:
        force_air = -0.5*C*A*rho*mag2(rocket.mom/mass)*norm(rocket.mom)
        if (time > 0.5) and (time <5.5):
            thrust_force = 100*norm(rocket.mom)
            force_total = force_g + thrust_force + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt                              
        else:
            force_total = force_g + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt
            
    if thrust == True and drag == True and loss == True:
        force_air = -0.5*C*A*rho*mag2(rocket.mom/mass)*norm(rocket.mom)
        if (time > 0.5) and (time <5.5):
            force_g = mass*g
            thrust_force = 100*norm(rocket.mom)
            force_total = force_g + thrust_force + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt
            mass = mass - fuel_loss*dt
    
        else:
            force_g = mass*g     
            force_total = force_g + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt
        
    rocket.vel = rocket.mom/mass
    
    if mag(rocket.vel) > max_speed:
        max_speed = mag(rocket.vel)
        
    y_pos_vs_x_pos_rocket.plot(pos = (rocket.pos.x, rocket.pos.y))
    y_vel_vs_t_rocket.plot(pos = (time, rocket.vel.y, ))
    

    
    time = time +dt
print(rocket.pos.x, 'm')    
print(time , 's')
print(max_speed , 'm/s')
