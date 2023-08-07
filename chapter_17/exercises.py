from datetime import datetime, date, time

################################
# Chapter 17, in-text exercises
################################

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    


class Time:
    '''Represents a time of day.
       Attributes: hour, minute, second
    '''
    def print_time(self):
        '''Takes a time object and prints it in format:
           hh:mm:ss
           Input: Time object
           Output: prints hh:mm:ss
        '''
        txt = '{:02.0f}:{:02.0f}:{:02.2f}'.format(self.hour, self.minute, self.second)
        print(txt)
    
    def pure_increment(self, seconds):
        '''Adds a number of seconds to a given time object and returns the new time
           Input: time object and seconds to add (integer)
           Output: input time is modified
        '''
        tnew = Time()
        tnew.second = self.second + seconds
        if (tnew.second >= 60):
            divider = tnew.second // 60
            remainder = tnew.second % 60
            tnew.second = remainder
            tnew.minute = time.minute + divider
        if (tnew.minute >= 60):
            divider = tnew.minute // 60
            remainder = tnew.minute % 60
            tnew.minute = remainder
            tnew.hour = time.hour + divider
        if (tnew.hour > 23):
            remainder = tnew.hour % 24
            tnew.hour = remainder
        return tnew
    
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds 


    def base60_increment(self, seconds):
        '''adds seconds to a time and returns the new time.
           Uses the time_to_int and int_to_time functions from the book.
           Input: time object, integer number of seconds
           Output: new time object
        '''    
        tnew = Time()
        tnewint = self.time_to_int() + seconds
        tnew = int_to_time(tnewint)
        return tnew
        
        
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int() 
    
class Point:
    '''Represents a point in 2D space.
       
       Attributes: x, y.
    '''
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({:.0f},{:.0f})'.format(self.x, self.y)
        
    def __add__(self, other):
        if isinstance(other, Point):
            return self.addPoints(other)
        else:
            return self.addTuple(other)
           
    def addPoints(self, other):
        newPoint = Point()
        newPoint.x = self.x + other.x
        newPoint.y = self.y + other.y
        return newPoint
               
    def addTuple(self, tup):
        newPoint = Point()
        newPoint.x = self.x + tup[0]
        newPoint.y = self.y + tup[1]
        return newPoint
        
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))        
        
here = Point(2,3)
there = Point(8,-1)
tupie = (12, 5)
print('here: ', here)
print('there: ', there)
print('tuple: ', tupie)
print(here + there)

print("Here comes the special addition!")
print(here + tupie)

print_attributes(there)
