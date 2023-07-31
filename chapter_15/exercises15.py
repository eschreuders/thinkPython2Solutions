import math

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
    
    box = Rectangle()
    box.width = 100
    box.height = 50
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0
    
    move_rectangle(box,10,20)
    print(box.corner.x, box.corner.y)
