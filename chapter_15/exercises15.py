import math

################################
# Chapter 15, in-text exercise
################################

class Point:
    '''Represents a point in 2D space.'''
    
    

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
    
    
if __name__ == '__main__':    
    ################################
    # Chapter 15, in-text exercise
    ################################
    Amsterdam = Point()
    Breda = Point()
    Amsterdam.x = 2
    Amsterdam.y = 4
    Breda.x = 3
    Breda.y = 2
    print(distance_between_points(Amsterdam, Breda))
