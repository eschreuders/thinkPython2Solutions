# 3-1
######################################################
# takes a string and fills in lead spaces so the last letter of the string is
#in column 70
def right_justify(s):
    number_spaces = 70-len(s)
    return_string = ' ' * number_spaces + s
    print(return_string)

right_justify('hello')
right_justify("it's me")


# 3-2
######################################################
# 1) take a nested function and test it

def do_twice(function):
    function()
    function()

def print_spam():
    print("Spam")

do_twice(print_spam)

# 2) Now do it twice with an argument

def do_twice_withcat(function, arg1, arg2):
    function(arg1, arg2)
    function(arg1, arg2)

def print_cats(firstcat, secondcat):
    print(firstcat + ' ' + secondcat)

do_twice_withcat(print_cats, 'Fluffy', 'Scritches')

# 3) Now play with print twice

def print_twice(bruce):
    print(bruce)
    print(bruce)
    
def do_twice_arg(function, argument):
    function(argument)
    function(argument)


# 4) do twice print twice with spam

do_twice_arg(print_twice, 'spam')

# 5) Do four

def print_catspam(string):
    print('spam '+ string)

def do_four(function, value):
    do_twice_arg(function,value)
    do_twice_arg(function,value)

do_four(print_catspam,'meow')


# 3-3 fully scalable because I'm awesome :)
######################################################


def fancy_grid(colwidth=4,colnum=2, rowheight=4, rownum=2):
    rowhead = '+ ' + "- "*colwidth
    rowbody = '| ' + '  '*colwidth
    fullinehead=rowhead * colnum + '+\n' 
    fullinebody=rowbody * colnum + '|\n'
    block = fullinehead + fullinebody*rowheight
    print(block*rownum,end='')
    print(fullinehead,end='')
    
fancy_grid()
fancy_grid(2,4,2,4)

fancy_grid(3,2,3,2)
