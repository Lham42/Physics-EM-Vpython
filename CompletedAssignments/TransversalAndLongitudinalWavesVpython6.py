# import graphing features
from __future__ import division 
from visual import *
from visual.graph import *

# dtime
t = 0
dt = 1e-15

# number of masses
n = 20

# Some constants
ang = 1e-10
amu = 1.66054e-27

# Initial conditions

m = 63*amu
L_0 = 2*ang #equilibrium length of a molecular bond
k = 20      # N/m spring constant between two molecules


atom = []   # array of copper atoms



#display
position_time = gdisplay( x = 600, y = 0,
                          title = "Position vs Time of the Second Last Atom",
                          xtitle = 'Time(s)', ytitle = "Position (m)",
                          foreground = color.black,
                          background = color.white)

r_t = gdots(gdisplay = position_time, color = color.blue)

#initialize the values for the molecules

for i in range(n):
    atom.append(sphere(pos = ((i-n/2)*L_0)*vector(1,0,0) , radius =L_0/3, color = color.red, mom = m*vector(0,0,0)))

atom[n-2].color = color.cyan

#stretch the first particle
stretch = -0.3*L_0*vector(1,0,0)
atom[1].pos = atom[1].pos + stretch


#count = 0

#delay 
#while count < 5:
   # rate(5)
   # count += 1

#Goes through each atom

while true:
    rate(500)
    r = atom[1].pos - atom[0].pos
    delta_x  = mag(r) - L_0
    r_hat = norm(r)
    f_right = k*(delta_x)*r_hat



    for i in range (1,n-1):
        f_left = -f_right
        r = atom[i+1].pos - atom[i].pos
        delta_x  = mag(r)-L_0
        r_hat = norm(r)
        f_right = k*(delta_x)*r_hat

        f_total = f_right + f_left

        # position and momentum update
        atom[i].mom = atom[i].mom + f_total*dt
        atom[i].pos = atom[i].pos + (atom[i].mom/m)*dt

        #plot
        r_t.plot(pos = (t,atom[n-2].pos.x - (n-4)*L_0/2))      #REMEMBER TO CHANGE TO Y FOR TRANVERSAL)

    t = t + dt
        
