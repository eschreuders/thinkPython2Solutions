"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle

def draw_pie_piece(t,angle,length):
    '''Draws an isosceles triangle based on the equal leg length and the top 
    angle. Starts at the top. Calculates base length.
    t: Turtle
    angle: Top angle in degrees
    length: Length of the legs of the isosceles triangle
    '''
    baselength = 2* math.sin(math.radians(angle/2))*length
    outerangle = (180-angle)/2
    t.fd(length)
    t.lt(180-outerangle)
    t.fd(baselength)
    t.lt(180-outerangle)
    t.fd(length)
    t.lt(180)
    
    
def draw_turtle_pie(t,npieces,radius):
    pieceangle = 360/npieces
    for i in range(npieces):
        draw_pie_piece(t,pieceangle,radius)    


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
    # circle(bob, radius)
   
    draw_turtle_pie(bob,8,150)
    # wait for the user to close the window
    turtle.mainloop()
