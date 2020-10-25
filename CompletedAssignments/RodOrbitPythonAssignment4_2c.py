
#Simulates a ball orbiting a thin steal rod
from __future__ import division
from visual import *
from visual.graph import *


#makes a rod
rod_length = 20
rod_radius = 0.1/2
rod_volume = pi*rod_radius**2*rod_length
rod_density = 8050 #density of steel in kg/m^3
mass_rod = rod_density*rod_volume
rod = cylinder(pos=(-10,0,0), axis=(2*rod_length,0,0), radius = rod_radius, length = rod_length, color = color.blue)


#Pick a point
test_mass = sphere(radius = 0.1, color = color.red, make_trail = True)
test_mass.pos = (0,1,1)
mass_test_mass = 5

#Gravity force
fscale = 0.001
G = 6.67e-11
total_force_by_rod = vector(0,0,0)
#farr = arrow(pos = test_mass.pos, axis= fscale*total_force_by_rod, color=color.yellow)
total_force = vector(0,0,0)


dm = 0.001 #m
volume_dm = dm*pi*rod_radius**2
mass_dm = rod_density*volume_dm
force_by_dm = (0,0,0)
#print(range_end)

#time
t = 0


print(mass_rod)
#Circular motion
r = test_mass.pos - rod.pos
v_circle = sqrt(G*mass_rod/mag(r))*vector(0,1,6)
initial_mom = 0.6*v_circle*mass_test_mass
test_mass.mom = initial_mom

dt = mag(test_mass.pos)/(20*mag(v_circle))


print(v_circle)
while true:
    rate(10000000)
    total_force_by_rod = vector(0,0,0)

    for a in arange(-rod_length/2,rod_length/2,dm):
        dm_pos = (a,0,0)
        r = test_mass.pos - dm_pos
        force_by_dm = -G*mass_dm*mass_test_mass/mag2(r)*norm(r)
        total_force_by_rod += force_by_dm

    total_force = total_force_by_rod
    #update momentum
    test_mass.mom += total_force*dt
    #update position
    test_mass.pos += (test_mass.mom/mass_test_mass)*dt
    t = t + dt
    

        
