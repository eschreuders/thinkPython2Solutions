"""
"""

from __future__ import print_function, division

import math
import time
import turtle


"""
Exercise 5-1
Script to calculate time of day and days passed since Epoch
"""
cur_time = time.time()
cur_time_seconds = cur_time // 1
print(cur_time_seconds, 'Seconds since Epoch ')
seconds_in_day = 60*60*24
print(seconds_in_day, "Seconds in a day")
days_since_epoch = cur_time_seconds//seconds_in_day
print(days_since_epoch, 'Days since Epoch')
time_in_seconds = cur_time_seconds % seconds_in_day
print(time_in_seconds, 'TOD in seconds')

hour_of_day = time_in_seconds//(60*60)
minute_of_day = (time_in_seconds % (60*60))//60
seconds_of_day = (time_in_seconds % (60*60)) % 60

print("It's now: ",hour_of_day," hours, ", minute_of_day, " minutes and", seconds_of_day, " seconds past midnight.")

"""
Exercise 5-2
Script to check Fermat's last theorem
"""
def check_fermat(a,b,c,n):   
    if n > 2:
        left = a**n + b**n
        right = c**n
        if left == right:
            print("Holy Smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")
    else:
        print("N is smaller than 2 or equal...")

check_fermat(3,6,9,3)
check_fermat(3,2,1,2)

def input_fermat():
    a = input("An input for a:\n")
    b = input("An input for b:\n")
    c = input("An input for c:\n")
    n = input("An input for n:\n")
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    check_fermat(a,b,c,n)
    
    
#input_fermat()


"""
Exercise 5-3
Script to check for triangles
"""

def is_triangle(A,B,C):
   if C > (A+B) or B > (A+C) or A > (B+C):
       print("No")
   else:
       print("Yes")
       
       
def input_is_triangle():
    A = input("Triangle leg A:\n")
    B = input("Triangle leg B:\n")
    C = input("Triangle leg C:\n")
    A = int(A)
    B = int(B)
    C = int(C)
    is_triangle(A,B,C)
    
#input_is_triangle()
#input_is_triangle()

"""
Exercise 5-4
Stack Diagrams


-------------------------

recurse(3,0):

__main__
recurse   n --> 3
          s --> 0
recurse   n --> 2
          s --> 3
recurse   n --> 1
          s --> 5
recurse   n --> 0
          s --> 6
          
output:
6

-------------------------
1)

recurse(-1,0) will trigger an infinite recursion as n will never reach 0

2)

recurse   n --> 5
          s --> 4
recurse   n --> 4
          s --> 9
recurse   n --> 3
          s --> 13
recurse   n --> 2
          s --> 16
          
Prints the n'th element of a series n+s with n decreasing by one each step and s_n-1 = n+s
n = number of steps to calculate
s = a base number 

"""


"""
Exercise 5-5
Mystery function

Makes a sort of angly spiral?

"""

def draw(t, length, n):
    if n == 0:
        return
    angle = 60
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n) 

"""
Exercise 5-5
Mystery function

Koch stuff

"""

def draw_koch(t, length):
    angle = 60
    lengthsmall = length/3
    if length < 10:
        t.fd(length)
        return
    else:
        draw_koch(t, lengthsmall)
        t.lt(60)
        draw_koch(t, lengthsmall)
        t.rt(120)
        draw_koch(t, lengthsmall)
        t.lt(60)
        draw_koch(t, lengthsmall)

def snowflake(t,length):
    draw_koch(t,length)
    t.rt(120)
    draw_koch(t,length)
    t.rt(120)
    draw_koch(t,length)
    
def draw_kochg(t, length, angle):
    anglec = 2*angle
    lengthsmall = length/3
    if length < 10:
        t.fd(length)
        return
    else:
        draw_kochg(t, lengthsmall, angle)
        t.lt(angle)
        draw_kochg(t, lengthsmall, angle)
        t.rt(anglec)
        draw_kochg(t, lengthsmall, angle)
        t.lt(angle)
        draw_kochg(t, lengthsmall, angle)

def snowflakeg(t,length, angle):
    for i in range(3):
        t.rt(120)
        draw_kochg(t,length, angle)

    
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
    
    snowflakeg(bob,200, 78)
    
    # wait for the user to close the window
    turtle.mainloop()
