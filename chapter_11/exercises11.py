from __future__ import print_function, division
import math
import random
import time



#
# Exercise intext: use get to make histogram more consise
#

def histogram(text):
    ''' Takes a string and returns a dictionary with the letters in it (keys) 
        and how many times they occur (values).
        
        text: the input string to check
        returns: dictionary with character:counter in the text 
    '''
    char_count = dict()
    for character in text:
        char_count[character] = char_count.get(character,0) + 1
    return char_count


print("Counting letters")
start_time = time.time()
result = histogram("Hello World! I am a monkey and I like bananas.")
print(result)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


#
# Exercise 11-1
#

def eng_dictionary():
    '''Takes a file of lines with strings and puts the strings as keys in a 
       dictionary. Values are set to True.
       
       uses: words.txt file (in runtime folder).
       
       returns: worddict, dictionary of strings in file words.txt as keys and 
       True as values.
    '''
    fin = open("../words.txt")
    worddict = dict()
    for line in fin:
        worddict[line.strip()] = True
    return worddict

def append_words():
    fin = open("../words.txt")
    wordlist = []
    for line in fin:
        wordlist.append(line.strip())
    return wordlist

def in_bisect(mylist, word):
    ''' Compares whether a given word appears before or after the middle of a 
        sorted list of words (alphabetically ascending). Then checks with the 
        half where the word should be until the word is found or the list 
        runs out and it isn't there. If the list has only two or less indices
        word is checked directly.
        
        mylist: A list of alphabetically ascending words
        word: the word you want to check for
        
        Returns: True if word is in mylist, false otherwise. 
    '''
    length = len(mylist)
    while length > 2:
        middle = int(len(mylist)/2)
        if mylist[middle] < word:
            mylist = mylist[middle : ]
            length = len(mylist)
        elif mylist[middle] > word: 
            mylist = mylist[0 : middle]
            length = len(mylist)
        elif mylist[middle] == word:
            return True
    return word in mylist    


# Filling the list and dictionary

print("filling list")
start_time = time.time()
wordlist = append_words()
print("--- %s seconds ---" % (time.time() - start_time))
print("Done!")

print("filling dictionary")
start_time = time.time()
worddict = eng_dictionary()
print("--- %s seconds ---" % (time.time() - start_time))
print("Done!")

# Do a lookup in both (bisection for the list, dict lookup for dictionary)

searchword = "yes"

print("bisection search")
start_time = time.time()
present = in_bisect(wordlist, searchword)
print(searchword, " is ", present)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

print("dictionary lookup")
start_time = time.time()
present = worddict.get(searchword,False)
print(searchword, " is ", present)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


#
# Exercise 11-2
#

def invert_dict(mydict):
    '''Inverts a dictionary from key:value to value:keys.
       Uses built in function setdefault()
       
       mydict: a dictionary to inverse
       Returns: inverse, the new, inverted dictionary.        
    '''
    inverse = dict()
    for key in mydict:
        val = mydict[key]
        print(key)
        inverse.setdefault(val,[]).append(key)
    return inverse
    
hist = histogram('parrot')

print("dictionary inversion without if statement")
start_time = time.time()
inverse = invert_dict(hist)
print(hist)
print(inverse)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

#
# Exercise 11-3
#

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
    
ack_dict = {}
        
def ack_mem(m, n):
    ''' Attempt to calculate ackermann with a memo dictionary
        Uses global ack_dict as memo. Trouble is, there's no significant reducing the recursion depth
    '''
    if (m,n) in ack_dict:   #SNEAKY TUPLE, >_> Not nice to newcomers, broke my brain on how to solve this one until I looked up the solution
        return ack_dict[m,n]
    elif m < 0 or n < 0:
        print("No, you're being negative!" )
        return
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack_mem(m - 1, 1)
    elif m > 0 and n > 0:
        ack_dict[m,n] = ack_mem(m-1, ack_mem(m, n-1)) 
        return ack_dict[m,n]


print("ACKERMAN")
start_time = time.time()
print(ack(3,4))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


print("ACKERMAN MEMO")
start_time = time.time()
print(ack_mem(3,4))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

#ack(4,5)
#ack(6,10)
ack(-1,3)


#
# Exercise 11-4
#


def has_duplicates(mylist):
    """Returns whether given sequence has duplicate values
       mylist: any list with possible duplicates
       returns: True or False
    """
    sortedlist = sorted(mylist)
    for i in range(1,len(sortedlist)):
        if sortedlist[i] == sortedlist[i-1]:
            return True
    return False
    
def improved_has_duplicates(mydict):
    '''Returns whether a given dictionary has duplicate keys
       mydict: any dictionary with possible duplicates
       returns: True or False
    '''
    memory = {}
    for key in sorted(mydict):
        if key in memory:
            return True
        else:
            memory[key] = True
    return False
    
    
print("duplicates list")
start_time = time.time()
print(has_duplicates(wordlist))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")    
    
    
    
print("duplicates dict")
start_time = time.time()
print(improved_has_duplicates(worddict))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")    
    
#
# Exercise 11-5
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
    
def rotate_pairs(mydict, n):
    '''Function that finds words that, rotated by n places, are still an english 
       word. Uses rotate_words funtion
       mydict: a dictionary of english words to check
       n: the amount of rotation to test with
       Returns: a dictionary of rotation pairs
    '''
    rotation_pairs = {}
    for key in mydict:
        val = rotate_word(key, n)
        if val in mydict:
            rotation_pairs[key] = val
    return rotation_pairs

print("rotation pairs n = -10")
start_time = time.time()
print(rotate_pairs(worddict, -10))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")    


#
# Exercvise 11-6
#

"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""




def read_dictionary(filename='c07b'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.
    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".
    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

"""
Encoding issues with the current dictionary version, so can't fully program this.

Pseudocode program:

puzzlerfinds = {}
mydict = {english word:pronunciation}
if word - first letter and word - second letter both exists in mydict
and (mydict[word - first letter] == mydict[word]) and (mydict[word - second letter] == mydict[word]) (Aristotle takes care of the rest :) )
puzzlerfinds[word] = True
"""
