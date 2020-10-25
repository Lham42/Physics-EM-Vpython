from __future__ import division
from visual import *
from visual.graph import * 

#Make the Room 12.192m x 6.096m x 6.096m

ball = sphere(pos=(3, 1, 2), radius= 0.057, color = color.black) #makes racquetball
wallR = box(pos=(6.1, 0, 0 ), size= (0.1, 6.1, 6.1) , color=color.green) # dimension  
wallL = box(pos=(-6.1, 0, 0 ), size= (0.1, 6.1, 6.1) , color=color.green)
wallB = box(pos=(0, 0, -3.05), size= (12.2, 6.1,  0.1) , color=color.red)
wallF = box(pos=(0, 0, 3.05), size= (12.2, 6.1,  0.1) , color=color.green, opacity=0.1)
wallT = box(pos=(0, 3.05, 0), size= (12.2, 0.1,  6.1) , color=color.green)
wallD = box(pos=(0, -3.05, 0), size= (12.2, 0.1,  6.1) , color=color.green)

#constants
deltat = 0.005
mass = 0.04
t = 0
gravity = vector(0, -9.8, 0)
Fair = (-2,0,-3)
force = mass*gravity
co_res = 0.83 # regulation racquetball has a coefficient of restitution of 0.82-0.85
bounce_count = 0
#Setting momentum
ball.momentum = vector(20*mass,15*mass,-12*mass)

#ball.momentum = vector(15,0,0)

#Graph

velocity_func = gdisplay( title = "Y position vs Y velocity",
                        xtitle = "y position",
                        ytitle = "y velocity",
                        xmin = -5, xmax =5,
                        ymin = -20, ymax = 20,
                        foreground = color.black,
                        background = color.white)
velocity = gcurve(gdisplay = velocity_func, color = color.black)



#ball tracker
vscale = 0.0005
varr = arrow(pos=ball.pos, axis=vscale*ball.momentum, color=color.yellow) #note where vscale is
ball.trail = curve(color=ball.color) 

while t < 30:
    rate(100)
    if ball.pos.x > wallR.pos.x -.1 and ball.momentum.x > 0:
        ball.momentum.x = -ball.momentum.x * co_res
        bounce_count += 1
    if ball.pos.x < wallL.pos.x + .1 and ball.momentum.x < 0:
        ball.momentum.x = -ball.momentum.x * co_res
        bounce_count += 1
    if ball.pos.z > wallF.pos.z -.1 and ball.momentum.z > 0:
        ball.momentum.z = -ball.momentum.z * co_res
        bounce_count += 1
    if ball.pos.z < wallB.pos.z +.1 and ball.momentum.z < 0:
        ball.momentum.z = -ball.momentum.z * co_res
        bounce_count += 1
    if ball.pos.y > wallT.pos.y -.1and ball.momentum.y > 0:
        ball.momentum.y = -ball.momentum.y * co_res
        bounce_count += 1
    if ball.pos.y < wallD.pos.y +.1 and ball.momentum.y < 0:
        ball.momentum.y = -ball.momentum.y* co_res
        bounce_count += 1
    if ball.momentum < 0.05:
        print(bounce_count, 'bounces')
        break
    
        
    ball.pos = ball.pos + (ball.momentum/mass)*deltat # position update
    ball.momentum = ball.momentum + force*deltat # momentum update
    varr.pos = ball.pos
    ball.trail.append(pos=ball.pos)
    varr.axis = vscale*ball.momentum
    t = t + deltat
    velocity.plot(pos= (ball.pos.y, (ball.momentum.y/mass)))
    

