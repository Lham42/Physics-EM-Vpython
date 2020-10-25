#Simulates a ball orbiting a thin steal rod

from __future__ import division
from visual import *
from visual.graph import *


#makes a rod
rod_length = 10
rod_radius = 0.1/2
rod_volume = pi*rod_radius**2*rod_length
rod_density = 8050 #density of steel in kg/m^3
mass_rod = rod_density*rod_volume
rod = cylinder(pos=(-rod_length,0,0), axis=(2*rod_length,0,0), radius = rod_radius, length = 2*rod_length, color = color.blue)


#Pick a point
test_mass = sphere(pos=(0,0,0), radius = 0.1, color = color.red)
test_mass.pos = (1,0.1,0.1)
mass_test_mass = 0.01


#Gravity force
G = 1#6.67e-11
total_force_by_rod = vector(0,0,0)
fscale = 1
farr = arrow(pos = test_mass.pos, axis= fscale*total_force_by_rod, color=color.yellow)

dm = 0.001
volume_dm = dm*pi*rod_radius**2
mass_dm = rod_density*volume_dm
force_by_dm = (0,0,0)


for a in arange(-rod_length,rod_length,dm):
    dm_pos = (a,0,0)
    r = test_mass.pos -dm_pos
    
    force_by_dm = -G*mass_dm*mass_test_mass/mag2(r)*norm(r)
    total_force_by_rod += force_by_dm
    
    #print(total_force_by_rod)
farr.axis = fscale*total_force_by_rod
print(total_force_by_rod)
print(mass_rod)
