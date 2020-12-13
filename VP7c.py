from __future__ import division
from visual import *
from visual.graph import * # graphing features

#simulation of a rocket

# time
t = 0
dt = 0.0001
dr = 0
W_T = 0

#information about the rocket
mass = 0.5                                  #mass of rocket (close to the apogee rocket cesaroni p38-3g mellow (I55) mass)
g = vector(0,-9.8,0)                    #acceleration due to gravity
force_g = mass*g                        #gravitational force


#Energy
U = 0
KE = 0
ET = 0
ET_initial = 0
ET_final = 0
ET_change = 0

#conditions:
thrust = True 
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

energy = gdisplay(title = "Energy of the system vs Time",          #Energy of the system
                        x=500, y=200,   
                        xtitle = "time(s)",
                        ytitle = "energy(J)",
                        foreground = color.black,
                        background = color.white)

y_pos_vs_x_pos_rocket = gdots(gdisplay = trajectory, color = color.blue)    # a graphics curve for y position vs x position
y_vel_vs_t_rocket = gdots(gdisplay = velocity, color = color.red)

#energy curves
KE_v_t =  gdots(gdisplay= energy, color = color.blue)               #kinetic
U_v_t =   gdots(gdisplay= energy, color = color.green)               #potential
ET_v_t =   gdots(gdisplay= energy, color = color.red)               #total

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
        if (t > 0.5) and (t <5.5):
            thrust_force = 100*norm(rocket.mom)
            force_total = force_g + thrust_force
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt                              
        else:
            thrust_force = 0
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_g)*dt
    if thrust == True and drag == True and loss == False:
        force_air = -0.5*C*A*rho*mag2(rocket.mom/mass)*norm(rocket.mom)
        if (t > 0.5) and (t <5.5):
            thrust_force = 100*norm(rocket.mom)
            force_total = force_g + thrust_force + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt                              
        else:
            thrust_force = 0
            force_total = force_g + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt
            
    if thrust == True and drag == True and loss == True:
        force_air = -0.5*C*A*rho*mag2(rocket.mom/mass)*norm(rocket.mom)
        if (t > 0.5) and (t <5.5):
            force_g = mass*g
            thrust_force = 100*norm(rocket.mom)
            force_total = force_g + thrust_force + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt
            mass = mass - fuel_loss*dt
    
        else:
            thrust_force = 0
            force_g = mass*g     
            force_total = force_g + force_air
            rocket.pos = rocket.pos + (rocket.mom/mass)*dt                      
            rocket.mom = rocket.mom + (force_total)*dt
            
    #Energy Calculations
    dr = dt * (rocket.mom/mass)
    KE = (mass*(mag(rocket.mom/mass)**2))/2
    U = mass*9.81*rocket.pos.y
    ET = KE + U
    W_T  = W_T + dot(dr,thrust_force)

    if t > 0.5 and t < 0.5 + dt:
        print("The initial total energy is: ", ET)
        ET_initial = ET
    if t> 5.5 and t < 5.5 +dt:
        print("The total energy after thrust is: ", ET)
        ET_final = ET
        ET_change = ET_final - ET_initial
        print ("The change in energy is: ", ET_change)
        print("The Work done by thrust, found numerically is: ", W_T)
    
            
    rocket.vel = rocket.mom/mass
    
    if mag(rocket.vel) > max_speed:
        max_speed = mag(rocket.vel)

    #plots 
    y_pos_vs_x_pos_rocket.plot(pos = (rocket.pos.x, rocket.pos.y))
    y_vel_vs_t_rocket.plot(pos = (t, rocket.vel.y))
    
    KE_v_t.plot(pos = (t, KE))
    U_v_t.plot(pos = (t, U))
    ET_v_t.plot(pos = (t, ET))

    
    t = t +dt
print(rocket.pos.x, 'm')    
print(t , 's')
print(max_speed , 'm/s')

