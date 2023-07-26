import turtle
#bob = turtle.Turtle()
#print(bob)

#for i in range(4):
#    bob.lt(90)
#    bob.fd(100)

#turtle.mainloop()

# 4-1
######################################################

def square(t):
    for i in range(4):
        t.lt(90)
        t.fd(100)

bob = turtle.Turtle()
print(bob)
square(bob)

# 4-2
######################################################

def square_length(t,length):
    for i in range(4):
        t.lt(90)
        t.fd(length)

square_length(bob,40)
#square_length(bob,150)
#square_length(bob,400)
#square_length(bob,75)

# 4-3
######################################################
def polygon(t,length,nsides):
    for i in range(nsides):
        t.lt(360/nsides)
        t.fd(length)

polygon(bob,600,3)
#polygon(bob,100,5)
#polygon(bob,80,4)
#polygon(bob,200,8)


# 4-4
######################################################
import math
print(math.pi)
def circle(t,radius):
    stepsize = (math.pi*2*radius)/360
    polygon(t,stepsize,360)

def circle2(t, radius):
    circumference = math.pi*2*radius
    nsides = int(circumference/3)
    polygon(t,3,nsides)
    
    
#circle(bob,100)
#circle2(bob,400)
circle2(bob,50)

# 4-4
######################################################

def arc(t,radius,angle):
    stepsize = (math.pi*2*radius)/360
    for i in range(angle):
        t.lt(1)
        t.fd(stepsize)
        
def polyline(t, length, nsides, angle):
    for i in range(nsides):
        t.lt(angle)
        t.fd(length)
        
def arc2(t,radius,angle):
    circumference = math.pi*2*radius
    arc_length = circumference*angle/360
    nsteps = int(arc_length/3)
    turnangle = 360/int(circumference/3)
    steplength = arc_length/nsteps
    polyline(t,steplength,nsteps,turnangle)

arc2(bob,100,145)
arc2(bob,40,200)
arc2(bob,300,120)
arc2(bob,50,360)


turtle.mainloop()

