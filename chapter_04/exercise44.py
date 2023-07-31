"""
"""

from __future__ import print_function, division

import math
import turtle

def do_twice(function):
    function()
    function()

def stripe(t,length):
    t.fd(length)
    
    
def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    
def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

    
def half_belly(t,halfheight):
    stripe(t,halfheight)
    arc(t,halfheight/2,180)
    
def reverse_half_belly(t,halfheight):
    arc(t,halfheight/2,180)
    stripe(t,halfheight)

    
def half_circle(t,halfheight):
    arc(t,halfheight/2,180)
    
def half_circle_r(t,halfheight):
    arc(t,halfheight/2,180)
    
def move_right(t, height):
    t.pu()
    t.rt(90)
    t.fd(height+0.25*height)
    t.lt(90)
    t.pd()


def draw_a(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    half_belly(t,halfl)
    half_belly(t,halfl)
    stripe(t,height-quartl)
    t.lt(180)
    stripe(t,height)
    t.pu()
    t.lt(180)
    t.fd(quartl)
    t.pd()

def draw_b(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    half_belly(t,halfl)
    t.lt(180)
    stripe(t,height)
    t.lt(180)
    stripe(t,height)
    half_belly(t,halfl)

def draw_c(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    t.pu()
    stripe(t,halfl)
    t.pd()
    half_circle(t,halfl)
    half_belly(t,halfl)

def draw_d(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    half_belly(t,halfl)    
    half_belly(t,halfl)
    stripe(t,halfl+height)
    t.lt(180)
    stripe(t,halfl+height)
    t.lt(180)
    
def draw_e(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    t.pu()
    stripe(t,halfl)
    t.lt(90)
    stripe(t,halfl)
    t.lt(180)
    t.pd()
    stripe(t,halfl)
    t.lt(90)
    half_circle(t,halfl)
    half_belly(t,halfl)    
    
def draw_f(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    t.pu()
    stripe(t,height)
    t.pd()
    half_circle(t,halfl)
    stripe(t,halfl)
    t.lt(90)
    stripe(t,quartl)
    t.lt(180)
    stripe(t,quartl)
    t.lt(90)
    stripe(t,halfl+quartl)
    t.pu()
    t.lt(90)
    stripe(t,halfl)
    t.lt(90)
    stripe(t,quartl)
    t.pd()
    
    
def draw_g(t,height=50):
    halfl = height/2
    quartl = height/4
    move_right(t,halfl)
    half_belly(t,halfl)
    half_belly(t,halfl)
    t.lt(180)
    stripe(t,height)
    t.rt(90)
    stripe(t,halfl)
    t.pu()
    t.lt(180)
    stripe(t,halfl)
    t.lt(90)
    stripe(t,height)
    t.pd()
    
# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw a circle centered on the origin
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    


    #draw_a(bob,60)
    #draw_b(bob,60)
    #draw_c(bob,60)
    #draw_d(bob,60)
    draw_e(bob,60)
    draw_f(bob, 60)
    draw_g(bob,60)
    # wait for the user to close the window
    turtle.mainloop()
