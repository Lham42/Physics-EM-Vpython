#  Plots relativistic Lamborghini 

from __future__ import division

from visual import *
from visual.graph import * # import graphing features

c = 340  #speed of light, greatly reduced


simulation_time = 100
t = 0
mass = 1000
accel = 1*9.8 
force = mass*accel  #applied force


velocity_function = gdisplay(  title = 'velocity vs. time',  
                    xtitle = 'time', xmin = 0, xmax = simulation_time,
                    ytitle = 'speed',
                    foreground=color.black,
                    background= color.white) #set display #1

distance_function = gdisplay(  x=0, y=400,
                    title = 'distance vs. time',  
                    xtitle = 'time', xmin = 0, xmax = simulation_time,
                    ytitle = 'distance',
                    foreground=color.black,
                    background= color.white) #set display #1
time_function = gdisplay(  x=600, y=400,
                    title = 'car time vs. observer time x',  
                    xtitle = 'observer time', xmin = 0, xmax = simulation_time,
                    ytitle = 'car time',
                    foreground=color.black,
                    background= color.white) #set display #1



vel_exact      = gcurve(gdisplay = velocity_function, color = color.black)  # analytic vel curve
vel_numerical_relativistic   = gdots(gdisplay = velocity_function, color = color.red) # numerical relativistic approx
vel_newtonian   = gcurve(gdisplay = velocity_function, color = color.green)  # exact newtonian approx
speed_light = gcurve(gdisplay = velocity_function, color = color.cyan)

position_exact      = gcurve(gdisplay = distance_function, color = color.black)  # analytic vel curve
position_numerical_relativistic   = gdots(gdisplay = distance_function, color = color.red) # numerical relativistic approx
position_newtonian   = gcurve(gdisplay = distance_function, color = color.green)  # exact newtonian approx

time_exact      = gcurve(gdisplay = time_function, color = color.black)  # analytic vel curve
time_numerical_relativistic   = gdots(gdisplay = time_function, color = color.red) # numerical relativistic approx
time_newtonian   = gcurve(gdisplay = time_function, color = color.green)  # exact newtonian approx


      
dt = .1  #graphing time increment

vel_relativistic = 0
position_relativistic = 0
classical_pos = 0
time_numerical_rel = 0
momentum = 0
count = 0

while (t < simulation_time):
    rel_vel =  (momentum/mass)/ sqrt(1 + (momentum/(mass*c))**2) #find rel velocity from momentum
    gamma =  1/(sqrt(1-(rel_vel/c)**2)) #find gamma from rel_vel or momentum
    
    classical_vel = (momentum/mass)                           #find classical velocity from momentum
    exact_rel_vel =  c*(((force*t)/(mass*c))/(sqrt(1+((force*t)/(mass*c))**2)))      #analytic solution to relativistic v(t)

    classical_pos =  classical_pos + ((classical_vel)*dt)                   #classical exact position for solution constant F, think high school
    exact_rel_pos = (mass*c**2)*(sqrt(1+((force*t)/(mass*c))**2))/(force) - (mass*c**2)/(force) 

    momentum = momentum + force*dt                      #momentum update

    position_relativistic =  position_relativistic + ((momentum/mass)/(sqrt(1+(momentum/(mass*c))**2)))*dt    #numerical relativistic position update
    time_numerical_rel +=  dt/gamma    #numerical relativistic time update
    exact_time_relativistic =  ((mass*c)/(force))*log(((force*t)/(mass*c))+ sqrt(1+((force*t)/(mass*c))**2)) #analytic solution to relativistic time


    if (count % 20 == 0):    #plot every 20 time steps
        vel_exact.plot (pos=(t, exact_rel_vel ))        # analytic rel vel
        vel_numerical_relativistic.plot  (pos=(t,rel_vel))   # numerical rel vel
        vel_newtonian.plot  (pos=(t,classical_vel))   # analytic classical vel
        
        position_exact.plot  (pos=(t,exact_rel_pos))   # analytic rel pos
        position_numerical_relativistic.plot  (pos=(t,position_relativistic))   # numerical rel pos
        position_newtonian.plot  (pos=(t,classical_pos))   # analytic classical pos
        
        speed_light.plot (pos=(t,c))
        
        time_exact.plot (pos=(t,exact_time_relativistic))  #analytic rel time
        time_numerical_relativistic.plot (pos=(t,time_numerical_rel)) #numerical rel time
        time_newtonian.plot (pos=(t,t))        #classical time

    t = t + dt  #advance to next classical time point
    count += 1
