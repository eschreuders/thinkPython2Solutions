import math
import copy
import turtle

################################
# Chapter 15, in-text exercises
################################

class Point:
    '''Represents a point in 2D space.
       
       Attributes: x, y.
    '''

class Rectangle:
    '''Represents a rectangle, defined by width, height and coordinates of the 
       lower left corner
       
       Attributes: width, height, corner
    '''

class Circle:
    '''Represents a circle with a redius and center coordinates.
    
       Attributes: radius, center
    '''


def distance_between_points(point1, point2):
    '''Takes two point objects and calculates the distance between them.
    uses: math
    input: two point objects with x and y coordinates assigned.
    output: numeric distance between the points.
    '''
    dx = abs(point1.x - point2.x)
    dy = abs(point1.y - point2.y)
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def move_rectangle(rectangle, dx, dy):
    '''Moves a Rectangle object in the x and y coordinate space.
       Use negative dx and dy for moving left or down!
       uses: 
       Input: rectangle object, <dx> and <dy> both numeric
       Output: Modified rectangle object (<corner has changed>)
    '''
    rectangle.corner.x = rectangle.corner.x + dx
    rectangle.corner.y = rectangle.corner.y + dy
    
def move_copy_rectangle(rectangle, dx, dy):
    '''copies a Rectangle object and moves the copy in the x and y coordinate 
       space. Use negative dx and dy for moving left or down!
       uses:   copy
       Input:  rectangle object, <dx> and <dy> both numeric
       Output: Modified copy of rectangle object (<corner has changed>)
    '''
    copyrect = copy.deepcopy(rectangle)
    copyrect.corner.x = copyrect.corner.x + dx
    copyrect.corner.y = copyrect.corner.y + dy
    return copyrect
    
################################
# Chapter 15 - 1 
################################    
    
def point_in_circle(circle, coord):
    '''Takes a circle object and Point object and checks whether the coordinate
       lies in the circle. Checks whether distance between center and point is
       smaller than the circle radius.
       uses: math
       Input: circle object and point object
       Output: boolean
    '''    
    dist = distance_between_points(circle.center,coord)
    return dist <= circle.radius
    
def rect_in_circle(rectangle, circle):
    '''Takes a rectangle and a circle object and checks whether the entire
       rectangle is in the circle. Leans on assumption: if all corners are
       in, the whole rectangle is in.
       uses: math
       Input: rectangle object and a circle object
       Output: Boolean
    '''
    testpoint = copy.copy(rectangle.corner)
    contained = point_in_circle(circle,testpoint)
    if contained == True:
        testpoint.x = testpoint.x + rectangle.width
        contained = point_in_circle(circle,testpoint)
        if contained == True:
            testpoint.y = testpoint.y + rectangle.height
            contained = point_in_circle(circle,testpoint)
            if contained == True:
                testpoint.x = testpoint.x - rectangle.width
                contained = point_in_circle(circle,testpoint)
    return contained
    
def rect_circle_corner(rectangle, circle):
    '''Takes a rectangle and a circle object and checks whether they
       overlap. Leans on assumption: if any corner is in the circle, it does
       uses: math
       Input: rectangle object and a circle object
       Output: Boolean
    '''
    testpoint = copy.copy(rectangle.corner)
    contained = point_in_circle(circle,testpoint)
    testpoint.x = testpoint.x + rectangle.width
    if point_in_circle(circle,testpoint):
        contained = True
    testpoint.y = testpoint.y + rectangle.height
    if point_in_circle(circle,testpoint):
        contained = True
    testpoint.x = testpoint.x - rectangle.width
    if point_in_circle(circle,testpoint):
        contained = True
    return contained

################################
# Chapter 4, too lazy for import today
################################
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


################################
# Chapter 15-2
################################

def draw_rect(t, rectangle):
    '''Takes a rectangle object and uses a turtle to draw it
       uses: turtle
       Input: rectangle object and a turtle object
       Output: rectangle drawn by turtle
    '''
    t.penup()
    t.seth(0)
    t.fd(rectangle.corner.x)
    t.lt(90)
    t.fd(rectangle.corner.y)
    t.rt(90)
    t.pendown()
    for i in range(2):
        t.fd(rectangle.width)
        t.lt(90)
        t.fd(rectangle.height)
        t.lt(90)
    t.seth(0)

def draw_circle(t,circle):
    '''Takes a turtle object and a circle. Draws the circle at the right
       coordinates. 
       uses: turtle
       Input: Turtle object and Circle object
       Output: Turtle drawing.
    '''
    t.seth(0)
    t.penup()
    t.fd(circle.center.x)
    t.lt(90)
    t.fd(circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pendown()
    arc(t, circle.radius, 360)
    t.rt(90)


        
if __name__ == '__main__':    
    ################################
    # Chapter 15, in-text exercises
    ################################
    Amsterdam = Point()
    Breda = Point()
    Amsterdam.x = 2
    Amsterdam.y = 4
    Breda.x = 3
    Breda.y = 2
    print(distance_between_points(Amsterdam, Breda))
    
    #make and move a box!
    box = Rectangle()
    box.width = 100
    box.height = 50
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0
    
    move_rectangle(box,10,20)
    print(box.corner.x, box.corner.y)
    
    #copy the box and move the copy!
    box2 = move_copy_rectangle(box, -20, 50)
    print('old friend: ', box.corner.x, box.corner.y)
    print('new friend: ', box2.corner.x, box2.corner.y)
     
    ################################
    # Chapter 15 - 1 
    ################################ 
    mycircle = Circle()
    mycircle.radius = 75
    mycircle.center = Point()
    mycircle.center.x = 150
    mycircle.center.y = 100
    
    checkpoint = Point()
    checkpoint.x = 160
    checkpoint.y = 70
    
    #make and move a box!
    box3 = Rectangle()
    box3.width = 30
    box3.height = 30
    box3.corner = Point()
    box3.corner.x = 135
    box3.corner.y = 85
    
    #point in circle
    print("Testing points in circles")
    print(point_in_circle(mycircle,Breda))
    print(point_in_circle(mycircle,checkpoint))
    
    #rectangle in circle
    print("testing rectangles in circles")
    print(rect_in_circle(box,mycircle))
    print(rect_in_circle(box2,mycircle))
    print(rect_in_circle(box3,mycircle))
    
    #rectangle corner in circle
    print("testing rectangle corners in circles")
    print(rect_circle_corner(box,mycircle))
    print(rect_circle_corner(box2,mycircle))
    print(rect_circle_corner(box3,mycircle))
    
    
    ################################
    # Chapter 15 - 2
    ################################ 
    bob = turtle.Turtle()
    
    draw_rect(bob,box)
    bob.penup()
    bob.home()
    bob.pendown()
    
    draw_rect(bob,box2)
    bob.penup()
    bob.home()
    bob.pendown()
    
    draw_rect(bob,box3)
    bob.penup()
    bob.home()
    bob.pendown()
    
    draw_circle(bob, mycircle)
    

    # wait for the user to close the window
    turtle.mainloop()
    
 
    
