from __future__ import division
from visual import *
from visual.graph import *  # graphing features

#I need:
#the motion
#center of mass
#graph the x and y components of the incident proton
#momentum of He nucleus
#total momentum of the system
#plot of scattering angle

dt = 1e-24
t= 0
k = 8.988e9     #coloumb's constant
AMU = 6.67e-27  #atomic mass unit
e = 1.6e-19     #elementary charge
femto = 1e-15   #femto meter
c = 3e8         #speed of light in a vacuum

#charges
q_proton = -e
q_he = 2*e

#masses
proton_mass = 1*AMU
he_mass = 4*AMU


#position
b = 2*femto           #impact parameter

init_pos_proton = vector(-20*femto,b,0)
init_pos_he = vector(0,0,0)


#dispays

Lab = display( title = 'Lab Frame',
               background= color.black)

xmom1 = gdisplay(x = 0, y = 0,
                title = 'X-Momentum vs Time of Proton',
                xtitle = 'time', ytitle = 'x-Momentum',
                foreground = color.black,
                background = color.white)

ymom1 = gdisplay(x = 0, y = 0,
                title = 'Y-Momentum vs Time of Proton)',
                xtitle = 'time', ytitle = 'Y-Momentum',
                foreground = color.black,
                background = color.white)

xmom2 = gdisplay(x = 0, y = 0,
                title = 'X-Momentum vs Time of Helium Nucleus)',
                xtitle = 'time', ytitle = 'Momentum',
                foreground = color.black,
                background = color.white)

ymom2 = gdisplay(x = 0, y = 0,
                title = 'Y-Momentum vs Time of Helium Nucleus)',
                xtitle = 'time', ytitle = 'Momentum',
                foreground = color.black,
                background = color.white)

sum_mom = gdisplay(x = 0, y = 0,
                title = 'Total Momentum vs Time of System',
                xtitle = 'time', ytitle = 'Total Momentum',
                foreground = color.black,
                background = color.white)

trajectory = gdisplay(x = 0, y = 0,
                title = 'Trajectory of Helium and Proton',
                xtitle = 'x', ytitle = 'y',
                foreground = color.black,
                background = color.white)

xmom1_time = gdots(gdisplay= xmom1, color = color.blue)
ymom1_time = gdots(gdisplay= ymom1, color = color.red)
xmom2_time = gdots(gdisplay= xmom2, color = color.blue)
ymom2_time = gdots(gdisplay= ymom2, color = color.red)
sum_mom_time = gdots(gdisplay = sum_mom, color = color.green)
trajectory_he = gdots(gdisplay = trajectory, color = color.red)
trajectory_pro= gdots(gdisplay = trajectory, color = color.blue)


#making the objects
proton = sphere(display = Lab, pos = init_pos_proton, radius = 0.7*femto, color = color.red, make_trail = True)
he = sphere(display = Lab, pos = init_pos_he, radius = 1.3*femto, color = color.cyan, make_trail =True)

#initial conditions
init_vel_proton = vector(0.05*c,0,0) #arbitrary, you can change
init_vel_he = vector(0,0,0)

proton.mom = init_vel_proton*proton_mass
he.mom = init_vel_he*he_mass

while t < 1e-20 :
    rate(100000)

    #force update
    r = proton.pos -  he.pos
    f_e = ((k*q_proton*q_he)/(mag2(r)))*norm(r)

    #momentum updates:
    proton.mom = proton.mom + f_e*dt
    he.mom = he.mom + (-f_e)*dt
    sum_mom = he.mom + proton.mom

    #position updates:
    proton.pos = proton.pos + (proton.mom/proton_mass)*dt
    he.pos = he.pos + (he.mom/he_mass)*dt

    #plots
    xmom1_time.plot(pos =(t,proton.mom.x))
    ymom1_time.plot(pos =(t,proton.mom.y))
    xmom2_time.plot(pos =(t,he.mom.x))
    ymom2_time.plot(pos =(t,he.mom.y))
    sum_mom_time.plot(pos =(t,mag(sum_mom)))
    trajectory_pro.plot(pos =(proton.pos.x,proton.pos.y))
    trajectory_he.plot(pos =(he.pos.x,he.pos.y))

    #increment time
    t = t + dt
    
