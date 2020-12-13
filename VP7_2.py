
from __future__ import division
from visual import *
from visual.graph import *

h = 8848 #altitude of mount everest

dt = 1
t = 0
m_earth = 5.977e24
m_object = 100
r_earth = 6.37817e6
g = vector(0,-9.8,0)
G = 6.67e-11

thing = sphere(pos = (0,r_earth+h,0), radius = 100, color = color.blue, make_trail = True)
earth = sphere (pos = (0,0,0), radius = 6e6, color = color.red)

KE = 0
U = 0
ET = 0

force_g = 0
force_total = 0

init_vel = vector(9500,0,0)
thing.mom = m_object*init_vel

trajectory = gdisplay(title = "y vs x position",
                      xtitle = 'x-position (m)',
                      ytitle = 'y-position(m)',
                      x = 0, y = 0,
                      foreground = color.black,
                      background = color.white)

energy = gdisplay(title = "Energy of the system",
                  xtitle = 'time(s)', ytitle = 'energy',
                  x = 0, y = 0,
                  foreground = color.black,
                  background = color.white)


y_v_x = gdots(gdisplay = trajectory, color = color.black)

KE_v_t = gdots(gdisplay = energy, color = color.red)
U_v_t =  gdots(gdisplay = energy, color = color.black)
ET_v_t = gdots(gdisplay = energy, color = color.blue)

while mag(thing.pos - earth.pos) > r_earth :
    rate(1e9)
    r = (thing.pos - earth.pos)
    force_g = -((G*m_earth*m_object)/(mag2(r)))*norm(r)
    force_total = force_g 

    #momentum update
    thing.mom = thing.mom + force_total*dt
    thing.pos = thing.pos + (thing.mom/m_object)*dt

    #Energy
    KE = 0.5*(m_object*mag2(thing.mom/m_object))
    U =  -((G*m_earth*m_object)/(mag(r))) #G*m_object*m_earth/mag(thing.pos)
    ET = U + KE
    
    #plot
    KE_v_t.plot(pos =(t, KE))
    U_v_t.plot(pos =(t, U))
    ET_v_t.plot(pos = (t,ET))
    y_v_x.plot(pos = (thing.pos.x,thing.pos.y))
    
    t = t + dt
    
