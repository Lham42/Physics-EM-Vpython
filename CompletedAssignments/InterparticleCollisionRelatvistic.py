from __future__ import division
from visual import *
from visual.graph import *  # graphing features


dt = 1e-24
k = 8.988e9     #coloumb's constant
AMU = 6.67e-27  #atomic mass unit
e = 1.6e-19     #elementary charge
femto = 1e-15   #femto meter
c = 3e8         #speed of light in a vacuum

#charges
q_proton = e
q_he = 2*e

#masses
proton_mass = 1*AMU
he_mass = 4*AMU


#position
b = 0*femto           #impact parameter

init_pos_proton = vector(-20*femto,b,0)
init_pos_he = vector(0,0,0)
init_pos_CM = (proton_mass*init_pos_proton + he_mass*init_pos_he)/(he_mass+proton_mass)

#dispays

Lab = display( title = 'Lab Frame',
               background= color.black)

#making the objects
proton = sphere(display = Lab, pos = init_pos_proton, radius = 0.8*femto, color = color.red, make_trail = True)
he = sphere(display = Lab, pos = init_pos_he, radius = 1.3*femto, color = color.cyan, make_trail =True)
CM = sphere(display = Lab, pos = init_pos_CM, radius = 0.1*femto, color = color.white, make_trail =True)

#initial conditions
init_vel_proton = vector(0.05*c,0,0) #arbitrary, you can change
init_vel_he = vector(0,0,0)

proton.mom = init_vel_proton*proton_mass
he.mom = init_vel_he*he_mass

while true:
    rate(2000)

    #force update
    r = proton.pos -  he.pos
    f_e = ((k*q_proton*q_he)/(mag2(r)))*norm(r)

    #momentum updates:
    proton.mom = proton.mom + f_e*dt
    he.mom = he.mom + (-f_e)*dt
    CM.mom = he.mom + proton.mom

    #position updates:
    proton.pos = proton.pos + ((proton.mom/proton_mass)/sqrt(1+(mag(proton.mom)/(proton_mass*c))**2))*dt
    he.pos = he.pos  + ((he.mom/he_mass)/sqrt(1+(mag(he.mom)/(he_mass*c))**2))*dt
    CM.pos = (proton_mass*proton.pos + he_mass*he.pos)/(he_mass+proton_mass)
    

    if(proton.pos.x >= (he.pos.x - 1.3*femto)):
        print(proton.mom/proton_mass)
        
    
    
