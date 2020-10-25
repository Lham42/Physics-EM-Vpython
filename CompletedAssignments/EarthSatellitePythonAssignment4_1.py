

#  Explores the gravitational forces between Earth and Moon

from __future__ import division

from visual import *
from visual.graph import * # import graphing features

G = 6.67e-11
mass_earth = 5.97e24
mass_moon  = 5.35e3
moon_apogee = 405503e3  #apogee of moon, farthest distance from earth meters

scene = display(center = (0,0,0), background = color.white)

initial_vel_earth = vector(0,0,0)
initial_mom_earth = mass_earth*initial_vel_earth
initial_pos_earth = vector(0,0,0)
radius_earth = 6371e3


#Graphing Stuff

trajectory = gdisplay(title = 'Y position vs X position',
                      xtitle = 'x position (m)', ytitle = 'y position (m)',
                      x = 0, y = 0, width = 1000, height = 500,
                      foreground = color.black,
                      background = color.white)
y_v_x = gdots(display = trajectory, color = color.blue)


initial_pos_moon = vector(0,moon_apogee,0)
radius_moon = 30


moon_object = sphere(pos=initial_pos_moon,
                     radius = radius_moon,
                     color = color.red,
                     make_trail = True )

earth_object = sphere(pos=initial_pos_earth,
                      radius = radius_earth,
                      opacity = .3,
                      color = color.blue,
                      make_trail = True )

pos_moon = initial_pos_moon


pos_earth = initial_pos_earth
mom_earth = initial_mom_earth

time = 0
dt = 100
r = pos_moon - pos_earth
v_circle = sqrt(G*mass_earth/mag(r))
initial_vel_moon = vector(v_circle,0,0) #0.78*v_circle
initial_mom_moon = mass_moon*initial_vel_moon
mom_moon = initial_mom_moon
Force_moon_by_earth = -G*mass_moon*mass_earth/mag2(r)*norm(r)

#Arrows:
ratio = (mag(Force_moon_by_earth))/mass_moon / ((mag(mom_moon))/mass_moon)
vscale = 2E5
fscale = 3E10
varr= arrow(pos=pos_moon, axis= vscale*(mom_moon/mass_moon), color=color.yellow)
Aarr= arrow(pos =pos_moon, axis = fscale*Force_moon_by_earth/mass_moon, color=color.blue)
#print(mom_moon/mass_moon,Force_moon_by_earth/mass_moon,)
print(initial_vel_moon)

while (mag(r) > radius_earth + radius_moon):
    rate(100000)
    r = pos_moon - pos_earth
    Force_moon_by_earth = -G*mass_moon*mass_earth/mag2(r)*norm(r) 
    mom_moon = mom_moon + Force_moon_by_earth* dt
    pos_moon = pos_moon + mom_moon/mass_moon * dt
    moon_object.pos = pos_moon
    #disp(Force_moon_by_earth)
    #disp(dot(Force_moon_by_earth,(mom_moon/mass_moon)))
    #Update the Arrows
    #ratio = (mag(Force_moon_by_earth)/mass_moon)/(mag(mom_moon)/mass_moon)
    #disp(ratio)
    #disp(mag(Force_moon_by_earth)/mass_moon, mag(mom_moon)/mass_moon)
    varr.pos = pos_moon
    varr.axis = vscale*(mom_moon/mass_moon)
    Aarr.pos = pos_moon
    Aarr.axis = fscale*(Force_moon_by_earth/mass_moon)
    #print (Aarr.axis)
    print((mag(mom_moon)/mass_moon )/(mag(Force_moon_by_earth)/mass_moon))
    #plot
    y_v_x.plot(pos = (pos_moon.x,pos_moon.y))
    #print(dot(mom_moon,Force_moon_by_earth)/mag(mom_moon)*mag(Force_moon_by_earth))

