
from __future__ import division
from visual import *
from visual.graph import *  # graphing features

G = 6.67e-11

m1 = 1e30 #mass of smaller star
m2 = 2e30 #mass of larger star


#period shit
t_orbit = 15*(24*60*60) # obrital period for both stars
w = 2*pi/t_orbit  #angular velocity
dt =  t_orbit/1000
t = 0           #time passed

#positions
a= ((G*m2)/(w*(1+(m1/m2)))**2)**(1/3) # distance of star 1 to center of mass (radius of orbit)
b= (m1/m2)*a # distance of star 2 to center of mass (radius of orbit) 
init_pos_s1 = vector(a,0,0)
init_pos_s2 = vector(-b,0,0)
init_pos_CM = ((m1*init_pos_s1.x + m2*init_pos_s2.x)/(m1+m2),0,0)
init_rel_pos = init_pos_s1 - init_pos_s2
print(a)


#displays
Lab = display( x=400, y = 0,
               title = "Lab Frame",
               background = color.black)

CM_Frame = display ( x = 800, y = 0,
                     title = "Center of Mass Frame",
                     background = color.black)

red_frame = display (x = 800, y = 300,
                     title = "Reduction to an Effective Single Body",
                     background = color.black)

xmom1 = gdisplay(x = 0, y = 0,
                title = 'X-Momentum vs Time of Star 1 (lighter star)',
                xtitle = 'time', ytitle = 'x-Momentum',
                foreground = color.black,
                background = color.white)

xmom2 = gdisplay(x = 0, y = 0,
                title = 'X-Momentum vs Time of Star 2 (heavier star)',
                xtitle = 'time', ytitle = 'x-Momentum',
                foreground = color.black,
                background = color.white)

sum_xmom = gdisplay(x = 0, y = 0,
                title = 'Total X-Momentum vs Time of System',
                xtitle = 'time', ytitle = 'Total Momentum',
                foreground = color.black,
                background = color.white)

arrows = display( x=0, y = 0,
               title = "Momenta of system",
               background = color.black)

xmom1_time = gdots(gdisplay= xmom1, color = color.blue)
xmom2_time = gdots(gdisplay= xmom2, color = color.red)
sum_xmom_time = gdots(gdisplay = sum_xmom, color = color.green)


#making the star objects
s1 = sphere(display = Lab, pos = init_pos_s1, radius = a/100, color = color.red, make_trail = True)
s2 = sphere(display = Lab, pos = init_pos_s2, radius = b/100, color = color.blue, make_trail = True)
C_Mass = sphere(display = Lab, pos = init_pos_CM, radius = b/100, color = color.yellow, make_trail = True)
rel_pos = sphere(display = Lab, pos = init_rel_pos, radius = b/100, color = color.yellow, make_trail = True)

#center of mass frame objects
s1_CM = sphere(display = Lab, pos = init_pos_s1, radius = a/100, color = color.red, make_trail = True)
s2_CM = sphere(display = Lab, pos = init_pos_s2, radius = b/100, color = color.blue, make_trail = True)
s1_CM.trail_object.display = CM_Frame
s2_CM.trail_object.display = CM_Frame

#Reduced frame objects
red = sphere(display = Lab, pos = init_rel_pos, radius = a/100, color = color.red, make_trail = True)
red.pos = init_pos_s1 - init_pos_s2
red.trail_object.display = red_frame


s1.trail_object.display = Lab
s2.trail_object.display = Lab
C_Mass.trail_object.display = Lab
rel_pos.trail_object.display = Lab

#initial conditions

alpha = 1.2  #star 1
beta = 1.0   #star 2

v1_init = (alpha*w*a)*vector(0,1,0)
v2_init = -(beta*w*b)*vector(0,1,0)
v1_cm =  0
v2_cm = 0

s1.mom = m1*v1_init
s2.mom = m2*v2_init
C_Mass.mom = s1.mom + s2.mom
sum_mom = s1.mom + s2.mom
sum_mom_x = s1.mom.x+s2.mom.x

red.mom = (m2*s1.mom - m1*s2.mom)/(m1+m2)

#Things I still need to do
#Center of Momentum Frame
#Moments of System
#Reduced Mass effective single particle

scale = 1

arrow1 = arrow(display = arrows, pos = (0,0,0), axis = scale*s1.mom, color=color.yellow)
arrow2 = arrow(display = arrows, pos = scale*s1.mom, axis = scale*s2.mom, color=color.blue)
arrow3 = arrow(display = arrows, pos = (0,0,0), axis = scale*sum_mom, color=color.red )

while t <= t_orbit*20:
    rate(2000)
    #force update
    r = s1.pos -s2.pos   #distance between two stars
    f_g = -((G*m1*m2)/(mag2(r)))*norm(r) #force of gravity between the stars  

    #momentum updates
    s1.mom = s1.mom +  f_g*dt
    s2.mom = s2.mom + (-f_g)*dt
    C_Mass.mom = s1.mom + s2.mom
    CM_vel = C_Mass.mom/(m1+m2)
    sum_mom_x = s1.mom.x+s2.mom.x
    sum_mom = s1.mom + s2.mom

    #position updates
    s1.pos = s1.pos + (s1.mom/m1)*dt
    s2.pos = s2.pos + (s2.mom/m2)*dt
    C_Mass.pos = (m1*s1.pos + m2*s2.pos)/(m1+m2)
    rel_pos.pos = s1.pos - s2.pos


    #Center of Mass frame updates
    v1_cm = (s1.mom/m1) - CM_vel
    v2_cm = (s2.mom/m2) - CM_vel

    s1_CM.pos = s1_CM.pos + v1_cm*dt
    s2_CM.pos = s2_CM.pos + v2_cm*dt

    #reduced frame
    red.pos = s1.pos - s2.pos

    
    #plot
    xmom1_time.plot(pos =(t,s1.mom.x))
    xmom2_time.plot(pos =(t,s2.mom.x))
    sum_xmom_time.plot(pos =(t,sum_mom_x))

    #arrows
    arrow1.axis = scale*s1.mom
    arrow2.axis = scale*s2.mom
    arrow3.axis = scale*sum_mom
    arrow2.pos = s1.mom
    #print(s1.pos.y, s2.pos.y)

    #increment time
    t += dt
