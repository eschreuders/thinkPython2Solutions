from datetime import datetime, date, time

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
    txt = '{:02.0f}:{:02.0f}:{:02.2f}'.format(timeobj.hour, timeobj.minute, timeobj.second)
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
    return time
    
def int_to_time24(seconds):
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
    
################################
# Chapter 16 exercise 1
################################

def mul_time(time, multiplier = 2):
    '''Takes a time object and returns a new object which is time
       multiplied by <multiplier>
       Input: Time object, multiplier integer
       Output: New Time object
    '''
    tnew = Time()
    tnewint = time_to_int(time) * multiplier
    tnew = int_to_time(tnewint)
    return tnew
    
def avg_pace(time, distance = 10):
    '''Takes a time object and returns a new object which is time
       divided by <distance>
       Input: Time object, distance integer
       Output: New Time object
    '''
    tnew = Time()
    tnewint = time_to_int(time) / distance
    tnew = int_to_time(tnewint)
    return tnew


################################
# Chapter 16 exercise 1
################################
def day_of_week():
    '''Takes current datetime object and returns the day of the week in a number.
       [0-6] where 0 is Monday
       Uses: datetime
       Input:
       Output: <weekday> integer
    '''
    now = datetime.now()
    return now.weekday()


def time_to_birthday(dt1):
   '''Calculates difference between a given date and now.
      uses: datetime
      input: <dt1> string of format {"%d/%m/%Y %H:%M:%S"}
      output: difference in {dd:hh:mm:ss}
   '''
   ndt2 = datetime.now()
   ndt1 = datetime.strptime(dt1, "%d/%m/%Y %H:%M:%S") 
   print('Your age is ', abs(ndt2 - ndt1))
   nbirthday = ndt1.replace(year = ndt2.year)
   print('Next birthday is ', nbirthday)
   if nbirthday <= ndt2:
       nbirthday = nbirthday.replace(year = (nbirthday.year + 1))
       print('Oops, real next birthday is ', nbirthday)    
   print('Which is in ',nbirthday - now)

def time_to_pass(dt1, dt2):
   '''Calculates difference between two given datetimes.
      uses: datetime
      input: <dt1> <dt2> both strings of format {"%d/%m/%Y %H:%M:%S"}
      output: difference in {dd:hh:mm:ss}
   '''
   ndt1 = datetime.strptime(dt1, "%d/%m/%Y %H:%M:%S") 
   ndt2 = datetime.strptime(dt2, "%d/%m/%Y %H:%M:%S") 
   delta = abs(ndt1 - ndt2)
   return delta #.strftime("%d/%m/%y %H:%M:%S")
   
   
def double_date(dto, dty, n = 2):
    '''Calculates the datetime on which the age of dt2 is n times that of dt1
       uses: datetime
       input: dt1 and dt2, both format {%d%m%Y}, <n> integer
       output: the date on which age2 is n*age1
    '''
    assert dto < dty
    t0 = datetime.min
    dateo = datetime.strptime(dto, "%d/%m/%Y")
    datey = datetime.strptime(dty, "%d/%m/%Y")
    dayo = dateo - t0
    dayy = datey - t0
    ntimesday = (dayo - n*dayy)/(1-n)
    print(ntimesday)

    ntimesdate = datetime.fromordinal(ntimesday.days)
    print(ntimesdate)
    print('\nThe date on which dto is {} times as old as dty is: '.format(n), ntimesdate)
    print('The ages in days will be {} and {} respectively.'.format(ntimesdate-dateo, ntimesdate - datey))


if __name__ == '__main__':

    ################################
    # Chapter 15, in-text exercises
    ################################
    time = Time()
    time.hour = 0
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
    incr = 3420 
    print('\nModifier incrementing by {:8.2f}'.format(incr))
    print_time(time3)
    increment(time3, incr )
    print_time(time3)
    
    #test pure increment time
    incr2 = 421 
    print('\nPure function incrementing by {:8.2f}'.format(incr2))
    print_time(time)
    print_time(pure_increment(time, incr2))
    
    #test b60 increment time
    incr3 = 421
    print('\nBase 60 function incrementing by {:8.2f}'.format(incr3))
    print_time(time)
    print_time(base60_increment(time, incr3))
    
    ################################
    # Chapter 16 exercise 1
    ################################
    
    m1 = 1.2
    print('\nMultiplying by {:02.1f}: '.format(m1))
    print_time(time2)
    print_time(mul_time(time2,m1))
    
    m2 = 3
    print('\nMultiplying by  {:02.1f}: '.format(m2))
    print_time(time)
    print_time(mul_time(time,m2))
    
    km = 10
    print('\nPace over {:02.1f}km: '.format(km))
    print_time(time)
    print_time(avg_pace(time,km))
    
    ################################
    # Chapter 16 exercise 2
    ################################
    print('\nPlaying with datetimes!')
    now = datetime.now()
    print('We are now: ', now)
    print('The day of the week is number: ',now.weekday())
    
    #With function (little bit redundant, but oh well...)
    print('\nWe are now on day {}'.format( day_of_week()))
    
    date1 = "21/11/2006 16:30:01"
    date2 = "21/12/2006 12:50:01"
    print('\nChecking the difference between two dates {} and {} :'.format(date1,date2))
    print(time_to_pass(date1,date2))
    
    birthday1 = "24/2/1989 19:05:00"
    print('\nChecking age and time to birthday for {}'.format(birthday1))
    time_to_birthday(birthday1)
    
    #small test to check whether I can muck around with timedeltas
    test = date.today()
    diff = test - test.min
    print(test.min + diff)
    
    print('\ngoing to calculate double dates')
    double_date("1/3/1967","4/3/1967",2)
    
    print('\ngoing to calculate double dates')
    double_date("24/11/1989","9/6/2018",3)
    
