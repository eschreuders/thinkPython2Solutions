import math

def print_backw(line):
    minindex = -len(line)
    index =    -1
    while index >= minindex:
        print(line[index])
        index = index - 1

print_backw("Hello World!")


for letter in "Apple":
    print(letter)
    
    
#
# Duck Script
#

prefixes = 'JKLMNOPQ'
suffix   = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix) 
        
        
fruit = 'banana'
print(fruit[:4])
print(fruit[2:])
print(fruit[:])


#
# Search letter in word, starting at given index...
#

def find_i(word, letter, index = 0):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1 
    
print(find_i("Biometrics","o"))
print(find_i("Biometrics","o",3))

#
# Search letter in word, starting...
#

def count(word, magicletter):
    count = 0
    for letter in word:
        if letter == magicletter:
            count = count + 1
    return count
    

print(count("banana", "n"))



#
# Exercise 8-1
#

print('mississippi'.rstrip('ips'))
print('norforblanorforblanorforblanor'.replace('norf','....',2))

#
# Exercise 8-2
#

print('banana'.count('a'))

#
# Exercise 8-3
# One liner is_palindrome

def is_palindrome(word):
    return word == word[::-1]
    

print(is_palindrome('noon'))
print(is_palindrome('banana'))

#
# Exercise 8-4
#

# 1) Just checks the first letter of s for lower case and returns the result. Brteaks after 1 iteration.

# 2) Always returns the string 'True' because it specifically checks if 'c' is a lowercase... which is... the case! Does not rewturn a boolean and breaks after first iteration.

# 3) Does loop the letters in s to check for lowercase every time, but only returns the result of the last letter.

# 4) Correct! returns True if any letter in the string s is lowercase. IF everything isn't then retuirns false

# 5) Checks if the whole word is lower case. It returns Flase as soon as a non-lower case letter is found. If the whole word has been checked and no falsies? Then returns True.

 
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('hello')) 

print(any_lowercase5('hELLO')) 

print(any_lowercase5('hellO')) 

print(any_lowercase5('hEllo')) 

#
# Exercise 8-5
# 

def rotate_word(s, n):
    s = s.lower()
    news = ''
    for c in s:
        c = ord(c) + n
        if 122-c < 0:
            c = 96 - (122-c)
        if 97-c > 0:
            c = 123 - (97-c)
        news = news + chr(c)
    return news 
    
rotate_word('yza',3)    
rotate_word('abc',-2)    
print(ord('a'), ord('z'))

print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
