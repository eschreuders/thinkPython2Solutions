from __future__ import print_function, division

import math

def compare(x,y):
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0

def is_ascending(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


print(compare(2,3))
print(compare(3,2))
print(compare(-1, -1))

print(is_ascending(1,2,3))
print(is_ascending(1,1,3))
print(is_ascending(1,2,1))

'''
Exercise 6-1

__main__
c    x --> 1   y --> 5   z --> 3   return --> 8100
b    z --> 9                       return --> 90                
a    x --> 9   y --> 9             return --> 90

Output:

9 90
8100

Let's check:
'''

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
    
def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y + 3, x + y))



'''
Exercise 6-2

Ackerman
'''

def ack(m, n):
    if m < 0 or n < 0:
        print("No, you're being negative!" )
        return
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1)) 

print(ack(3,4))
#ack(4,5)
#ack(6,10)
ack(-1,3)


'''
6-4 powers



'''

def is_power(a,b):
    print("recur",a % b, a, b)
    if a % b != 0:
        print("Hi, I'm false!")
        return False
    elif a % b == 0 and a > b:
        print("a mod b", a % b,"   a bigger b ", a > b)
        return is_power(a/b, b)
    elif a % b == 0 and a == b:
        print("Hi, I'm true!")
        return True
    else: 
        return False


       
       
print(2, 8, is_power(2,8),"\n")
print(8, 2, is_power(8,2),"\n")
print(16, 4, is_power(16,4),"\n")
print(16, 8, is_power(16,8),"\n")



'''
6-5 powers



'''
a = 20
b = 3
r = a % b
print(r)

def gcd(a,b):
    print("gcd:  ", a, b)
    if b == 0:
        return a
    else:
        r = a % b
        print("r: ", r)
        return gcd(b, r)


print(gcd(20,5), "\n")
print(gcd( 25, 20), "\n")
print(gcd( 253, 146), "\n")





