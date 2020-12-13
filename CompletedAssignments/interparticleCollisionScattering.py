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


#positio
init_pos_proton = vector(0,0,0)
init_pos_he = vector(0,0,0)


#dispays
Lab = display( title = 'Lab Frame',
               background= color.black)
angle_graph = gdisplay( x = 0, y = 0,
                        title = ' Angle of Scattering Vs Impact Parameter',
                        xtitle = 'Impact parameter (fm)', ytitle = 'Angle of scattering'
                        )


angle_v_b = gdots(gdisplay = angle_graph, color = color.blue)
#making the objects
he = sphere(display = Lab, pos = init_pos_he, radius = 1.3*femto, color = color.cyan, make_trail =True)



#choses impact parameters
#impact_parameters = [-0.05, -0.1, -0.15, -0.2, -0.25, -0.35, -0.5, -0.7, -1, -1.5, -2,-3,-4,-5,-6,-7,-8,-9,-10,0,0.05, 0.1, 0.15, 0.2, 0.25, 0.35, 0.5, 0.7, 1, 1.5, 2,3,4,5,6,7,8,9,10]
impact_parameters = [0,0.05, 0.1, 0.15, 0.2, 0.25, 0.35, 0.5, 0.7, 1, 1.5, 2,3,4,5,6,7,8,9,10, 12, 15 , 20]
for b in impact_parameters:

    #reset time
    time = 0

    #reset positions
    b = b*femto
    init_pos_proton = vector(-20*femto,b,0)
    init_pos_he = vector(0,0,0)
    
    #creates animation at each impact parameter
    proton = sphere(display = Lab, pos = init_pos_proton, radius = 0.7*femto, color = color.red, make_trail = True)
    
    #Reset velocities
    init_vel_proton = vector(0.05*c,0,0) #arbitrary, you can change
    init_vel_he = vector(0,0,0)
    
    #Resent momentums
    proton.mom = init_vel_proton*proton_mass
    he.mom = init_vel_he*he_mass

    #always set  position of helium nucleus to origin
    he.pos = init_pos_he
    
    while time < 3e-21:
        rate(100000)
        #force update
        r = proton.pos -  he.pos
        f_e = ((k*q_proton*q_he)/(mag2(r)))*norm(r)
        #momentum updates:
        proton.mom = proton.mom + f_e*dt
        he.mom = he.mom + (-f_e)*dt
        #position updates:
        proton.pos = proton.pos + (proton.mom/proton_mass)*dt
        he.pos = he.pos + (he.mom/he_mass)*dt

        time += dt

    cos_theta = dot(vector(1,0,0), norm(proton.mom))
    theta = acos(cos_theta)
    angle_v_b.plot(pos = (b/femto,theta*(180/pi)))
