import math

def print_n_rec(s,n):
    if n <= 0:
        return
    print(s)
    print_n_rec(s, n-1)

def print_n_loop(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n_rec("recursive four times", 4)
print_n_loop("loop four times", 4)

print(abs(4-3))
print(abs(4.5-3))
print(abs(3-4.000001))

#
# Exercise 7-1
#Square root approximation Table

def squarert(a, x, epsilon = 0.00001):
    '''Approximates the square root of a number based on an estimate.
    a: the number to approximate the square root of
    x: an estimate
    y: newly calculated estimate
    epsilon: approximation stops when y-x < epsilon
    '''
    while True:
#        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x= y
    return x


def test_square_root(nmin, nmax):     
    print("a   squarert(a)       math.sqrt(a)      diff")
    print("-   -----------       ------------      ----")       
    while nmin < nmax:
        if nmin == 1:
            est = 1
        else:
            est = nmin - 1 
        mysqrt = squarert(nmin, est, 0.0001)
        mathsqrt = math.sqrt(nmin)
        difference = abs(mysqrt-mathsqrt)
        print(nmin, mysqrt, mathsqrt, difference)
        nmin = nmin + 1
        
        
test_square_root(1.0,9.0)

#
# Exercise 7-2
# Evaluation loop


def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            break
        answer = eval(line)
        print(answer)
    return answer

#eval_loop()

#
# Exercise 7-3
# Approximate PI

def estimate_pi():
    k = 0
    x = 0.0
    y = 1.0
    while y >= 1e-15:
        y = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k)**4 * 396**(4*k))    
        x = x + y
        k = k + 1
    est_pi = 1/(x * 2 * math.sqrt(2)/9801)
    return est_pi
    
print(estimate_pi())
print(abs(estimate_pi() - math.pi))
