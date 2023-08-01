################################
# Chapter 16, in-text exercises
################################

class Time:
    '''Represents a time of day.
       Attributes: hour, minute, second
    '''
    
def print_time(timeobj):
    '''Takes a time object and prints it in format:
       hh:mm:ss
       Input: Time object
       Output: prints hh:mm:ss
    '''
    txt = '{:02d}:{:02d}:{:02d}'.format(timeobj.hour, timeobj.minute, timeobj.second)
    print(txt)
    
def is_after(time1, time2):
    ''' Returns True if t1 follows t2 chronologically and False otherwise.
        Input:  Two Time objects to compare
        Output: boolean
    '''
    after = time1.hour > time2.hour or \
    time1.hour == time2.hour and (time1.minute > time2.minute or \
    (time1.minute == time2.minute and time1.second > time2.second))    
    return after
    
def increment(time, seconds):
    '''Adds a number of seconds to a given time object.
       Input: time object and seconds to add (integer)
       Output: input time is modified
    '''
    time.second += seconds
    if (time.second >= 60):
        divider = time.second // 60
        remainder = time.second % 60
        time.second = remainder
        time.minute += divider
    if (time.minute >= 60):
        divider = time.minute // 60
        remainder = time.minute % 60
        time.minute = remainder
        time.hour += divider
    if (time.hour > 23):
        remainder = time.hour % 24
        time.hour = remainder

def pure_increment(time, seconds):
    '''Adds a number of seconds to a given time object and returns the new time
       Input: time object and seconds to add (integer)
       Output: input time is modified
    '''
    tnew = Time()
    tnew.second = time.second + seconds
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
    
    
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds 

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    if (time.hour > 23):
        time.hour = time.hour % 24
    return time
    
def base60_increment(time, seconds):
    '''adds seconds to a time and returns the new time.
       Uses the time_to_int and int_to_time functions from the book.
       Input: time object, integer number of seconds
       Output: new time object
    '''    
    tnew = Time()
    tnewint = time_to_int(time) + seconds
    tnew = int_to_time(tnewint)
    return tnew
    
    
if __name__ == '__main__':

    ################################
    # Chapter 15, in-text exercises
    ################################
    time = Time()
    time.hour = 23
    time.minute = 59
    time.second = 3
    print_time(time)

    time2 = Time()
    time2.hour = 11
    time2.minute = 59
    time2.second = 3
    
    time3 = Time()
    time3.hour = 12
    time3.minute = 40
    time3.second = 2
    
    print(is_after(time2, time3))
    
    time4 = Time()
    time4.hour = 0
    time4.minute = 0
    time4.second = 342
    
    #test increment time
    print_time(time3)
    increment(time3, 3420)
    print_time(time3)
    
    #test pure increment time
    print_time(time)
    print_time(pure_increment(time, 421))
    
    #test b60 increment time
    print_time(time)
    print_time(base60_increment(time, 421))
    
