
from __future__ import division
from visual import *
from visual.graph import *

ang = 1e-10
pico = 1e-12

r_c = 67*pico       #radius of carbon
r_o = 48*pico       #radius of oxygen
b_l = 116*pico #bond length of co
amu = 6.67e-27  #atomic mass unit

dt = 1e-17
t = 0

r_0 = 1.13*ang
u_0 = 1.8200726e-19

a = u_0*r_0**12
b = 2*u_0*r_0**6

k_eff = (72*u_0)/r_0**2


#graphics
energy1 = gdisplay(title = "Energy of the system vs Time (Lennard-Jones potential)",          #Energy of the system
                        x=500, y=200,   
                        xtitle = "time(s)",
                        ytitle = "energy(J)",
                        foreground = color.black,
                        background = color.white)
kinetic_energy1 = gdisplay(title = " Kinetic Energy of the system vs Time (Lennard-Jones potential)",          #Energy of the system
                        x=500, y=200,   
                        xtitle = "time(s)",
                        ytitle = "energy(J)",
                        foreground = color.black,
                        background = color.white)

kinetic_energy2 = gdisplay(title = "Kinetic Energy of the system vs Time (harmonic spring approximation)",          #Energy of the system
                        x=500, y=200,   
                        xtitle = "time(s)",
                        ytitle = "energy(J)",
                        foreground = color.black,
                        background = color.white)



energy2 = gdisplay(title = "Energy of the system vs Time (harmonic spring approximation)",          #Energy of the system
                        x=500, y=200,   
                        xtitle = "time(s)",
                        ytitle = "energy(J)",
                        foreground = color.black,
                        background = color.white)

seperation = gdisplay(title = "atom seperation over time",          #Energy of the system
                        x=500, y=200,   
                        xtitle = "time(s)",
                        ytitle = "seperation(m)",
                        foreground = color.black,
                        background = color.white)

#energy curves
KE_v_t =  gdots(gdisplay= kinetic_energy1, color = color.blue)               #kinetic blue
U_v_t =   gdots(gdisplay= energy1, color = color.green)               #potential green
ET_v_t =   gdots(gdisplay= energy1, color = color.red)               #total red

KE_v_t2 =  gdots(gdisplay= kinetic_energy2, color = color.blue)               #kinetic
U_v_t2 =   gdots(gdisplay= energy2, color = color.green)               #potential
ET_v_t2 =   gdots(gdisplay= energy2, color = color.red)               #total

as_t = gdots(gdisplay = seperation, color = color.black)
as_t2 = gdots(gdisplay = seperation, color = color.blue)


#making the atoms

o = sphere(pos = (0,0,0) , radius = r_o/10, color = color.blue, make_trail = True)
c = sphere(pos = (1.01*r_0,0,0), radius = r_c/10, color = color.red, make_trail = True)

o_2 = sphere(pos = (0,0.5*ang,0) , radius = r_o/10, color = color.blue, make_trail = True)
c_2 = sphere(pos = (1.01*r_0, 0.5*ang,0), radius = r_c/10, color = color.red, make_trail = True)

#initial Conditions
o.m = 16*amu
c.m = 12*amu

o.init_vel = vector(0,0,0) 
c.init_vel = vector(0,0,0)
o_2.init_vel = vector(0,0,0) 
c_2.init_vel = vector(0,0,0)

o.mom = o.init_vel*o.m
c.mom = c.init_vel*c.m
o_2.mom = o_2.init_vel*o.m
c_2.mom = c_2.init_vel*c.m

r = o.pos - c.pos

r_2 = o_2.pos - c_2.pos

while t < 8e-14: #true:
    rate(1e7)
    #update r
    r = o.pos - c.pos
    r_2 = o_2.pos - c_2.pos
    dr = mag(r) - r_0
    dr2 = mag(r_2) - r_0
    
    #force update
    f_o_by_c = -(((12*u_0)/r_0)*((r_0/mag(r))**7 - (r_0/mag(r))**13))*norm(r)
    f_c_by_o = -f_o_by_c
    
    f_o_by_c_2 = -k_eff*(mag(r_2)-r_0)*norm(r_2)
    f_c_by_o_2 = -f_o_by_c_2
    
    #momentum update
    o.mom += f_o_by_c*dt
    c.mom += f_c_by_o*dt
    o_2.mom += f_o_by_c_2*dt
    c_2.mom += f_c_by_o_2*dt


    #position update
    o.pos += (o.mom/o.m)*dt
    c.pos += (c.mom/c.m)*dt
    o_2.pos += (o_2.mom/o.m)*dt
    c_2.pos += (c_2.mom/c.m)*dt

    #energies
    KE = (c.m*(mag(c.mom/c.m)**2))/2 + (o.m*(mag(o.mom/o.m)**2))/2
    U = (a/(mag(r)**12)) - (b/(mag(r)**6)) + 1.82e-19
    ET = KE + U
    
    KE2 = (c.m*(mag(c_2.mom/c.m)**2))/2 + (o.m*(mag(o_2.mom/o.m)**2))/2
    U2 = 0.5*k_eff*((mag(r_2) - r_0)**2) 
    ET2 = KE2+U2

    KE_v_t.plot(pos = (t, KE))
    U_v_t.plot(pos = (t, U))
    ET_v_t.plot(pos = (t, ET))
    #print(ET)

    as_t.plot( pos = (t, dr))
    as_t2.plot( pos = (t, dr2))
    

    KE_v_t2.plot(pos = (t, KE2))
    U_v_t2.plot(pos = (t, U2))
    ET_v_t2.plot(pos = (t, ET2))
    #increment time
    t += dt
