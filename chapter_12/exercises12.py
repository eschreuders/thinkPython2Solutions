from __future__ import print_function, division
import math
import random
import time

#
# Exercise text sumall
#

def sumall(*args):
    '''Function that takes any number of arguments, gathers in a tuple
       and passes them to traditional sum function
       *args:   any number of numeric values
       Returns: numeric result of sum of arguments passed
    '''
    return sum(args)

print("sum all the arguments")
start_time = time.time()    
print(sumall(1,2,3,4.5))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


#
# Exercise 12-1
#

#global variable containing the lowercase alphabet
alphabet = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'

def hist_letters(text):
    '''Takes the letters of the alphabet and counts how often each letter 
       appears in a text. 
       global:  alphabet variable, tuple with all letters lowercase
                function 'sumall'
       text:    a letter-onlys tring to count the frequency of letters of. Case 
                doesn't matter, will be changed to lower. Takes out spaces, 
                comma's and periods.
       returns: tuple of tuples: (<'letter'>,<frequency>,<percentage>)       
    '''
    text = text.replace(' ','')
    text = text.replace('.','')
    text = text.replace(',','')
    tup = ()
    text = tuple(text.lower())    
    total = len(text)
    for letter in alphabet:
        counter = text.count(letter)
        tup = tup + (letter, counter, counter/total*100.)
    return tup
    
    
english = str(open("english.txt"))
nederlands = str(open("nederlands.txt"))
       
print(hist_letters(english))
print(hist_letters(nederlands))


#
# Exercise 12-2
#

def append_words(filename="../words.txt"):
    '''Opens a txt file of words, strips and returns a list of them
       takes: words.txt located in same path as this script.
       returns: list of cleaned words.
    '''
    fin = open(filename)
    wordlist = []
    for line in fin:
        wordlist.append(line.strip())
    return wordlist


print(tuple(sorted('hallo')))

def sorted_dictionary():
    '''Takes a global variable with words of the English language and 
       sorts the letters. Returns the sorted and the original word as 
       key:value pairs.Keys are unique, multiple values can be with a 
       key.
       Global: wordlist
       Returns: Dictionary of [tuple:list] format.
    '''
    sorted_words = dict()
    for word in wordlist:
        sorting = tuple(sorted(word))
        if sorting in sorted_words:
            #print(sorted_words[sorting])
            sorted_words[sorting].append(word)
        else:
            #print({sorting : [word]})
            sorted_words.update({sorting : [word]})
    return sorted_words
    
def print_multiples(dictionary):
    '''Takes a dictionary of keys with list values. If the value list
       has multiple elements, it prints the list.
       dictionary: A dicitionary with {<key>:<list>}
    '''    
    for key in dictionary:
        if len(dictionary[key]) > 1:
            print(dictionary[key])

print("Find all english anagrams!")
start_time = time.time()    
wordlist = append_words()  
sorted_english = sorted_dictionary()
print_multiples(sorted_english)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

#
# Exercise 12-2-2
#

def sort_multiples(dictionary):
    '''Takes a dictionary of keys with list values. Collects and sorts desc
       the values that are a list of length > 1. Returns the list of values.
       dictionary: A dicitionary with {<key>:<list>}
       Returns: List of lists. [<numelements>, [value list]]
    ''' 
    anagrams = dict()
    for key in dictionary:
        if len(dictionary[key]) > 1:
            anagrams.update({key: [len(dictionary[key]), dictionary[key]] })
    anagram_values = sorted(anagrams.values(), reverse = True)     
    final_sort = []   
    for i in anagram_values:
        final_sort.append(i[1])
    return final_sort
    
print("Find all english anagrams!")
anagrammes= sort_multiples(sorted_english)
print(anagrammes)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


#
# Exercise 12-2-3
#

def find_length(wordlists, length = 8):
    '''Takes a list of lists of words and a given integer. Returns the list element 
       where the first word has the given length and the number of elements is 
       highest.
       wordlists: list of lists of words [['','',...], ['','',...] ,...]
                  ASSUMPTION: list is sorted by length of elements, descending!
                  ...'cuz I'm lazy and already did the work during 12-2-2... 
       Returns: Prints the lists with a given length of the first word which 
       has the most elements.
    '''
    for words in wordlists:
        if len(words[0]) == length:
            print(words)
            return
            
print("8 letter anagram with most options, Scrabble BINGO!")
find_length(anagrammes)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")
            
#
# Exercise 12-3
#

def min_differences(word1, word2, num=2):
    '''Takes two strings of the same length and tests the number of differences 
       between them. If there are more than num, returns False, else True
       word1:   string
       word2:   string
       num:     integer
       returns: False if more than num differences or words are not the same 
                length, else True
    '''
    if len(word1) != len(word2):
        return False
    counter = 0
    for i in range(0,(len(word1)-1)):
        if word1[i] != word2[i]:
            counter = counter + 1
            if counter > 2:
                return False
    return True

print(min_differences('abcdefgh','abdceg'))

def test_anagram_diff(list_of_words, num = 2):
    '''takes a lists of words and checks all word elements for minimal 
       differences. Default is to check if there aren't more than n. Returns 
       the word combo's that pass the test.
       list_of_words: a list of words to test against each other for matches
       num: number of legal differences. Default is 2
       returns: matching word couples
    '''
    combos = []
    nwords = len(list_of_words)
    for i in range(0, nwords - 1):
        for j in range(i+1, nwords):     
            if min_differences(list_of_words[i], list_of_words[j]):
                combos.append([list_of_words[i], list_of_words[j]])               
    return combos

def loop_list_of_lists(list_of_lists, function):
    '''If you want to do something to all lists in a list, this is your friend.
       This setup is for the metathesis test but can be slightly altered for
       other purposes.
       list_of_lists: it's in the name. Applies a function to a list of lists
       return: a list of returns.
    '''
    outcomes = []
    for lists in list_of_lists:
        outcome = function(lists)
        if outcome != []:
            outcomes.append(outcome[0])
    return outcomes
       
            
print("Metathesis options!")
lala = loop_list_of_lists(anagrammes,test_anagram_diff)
print(len(lala))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")
                   
#
# Exercise 12-4
#

# dictionary: stores known reducible words.
reducible = {'':'','a':'a','i':'i'}

def find_child(pword):
    '''Takes a word and makes a list of all string possibilities if one
       letter is taken out.
       Variable: pword, a string, word to compute children of.
       Returns: a list of child words
    '''
    children = []
    for i in range(0,len(pword)):
        cword = list(pword)
        cword.pop(i)
        children.append(''.join(cword))
    print(children)
    return children
        
def is_reducible(pword):
    '''Takes a word and a dictionary of known reducible words. Chops out
       letters and checks if the new word is existing in the english language.
       If so, will check if with one letter less is existing, etc. If a child
       word is in the reducible dictionary, the parent will be added as well.
       Global variable: reducible, a dictionary of known reducable words.
       word: the word to be checked       
       Returns: a boolean is_reducible
    '''
    clist = find_child(pword)
    for cword in clist:
        print(cword)
        if cword in reducible:
            reducible.update({pword: pword}) 
            return True
        else:
            if cword in wordlist:
                print('nother round ', cword)
                return is_reducible(cword)
              
       
def find_reducibles():
    '''Takes the global list of English words and checks them all for reducability.
       Global:  wordlist, list of words in English language
       returns: dictionary of english reducable words and their length 
                formatted {<word>:<length>}
    ''' 
    reducible_words = []
    for word in wordlist:
        if is_reducible(word):
            reducible_words.append(word)
            reducible.update({word: word}) 
    return sorted(reducible_words)


                 
print("find reducible test!")
print(is_reducible('sprite'))
fout = open('output2.txt', 'w') 
fout.write('\n'.join(find_reducibles()))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")       

print("memory size ", len(reducible))
              
reducible_list = append_words("output.txt")
reducible_list = sorted(reducible_list, key = len, reverse = True)
print(reducible_list[0])
       
#for x in sorted_english.keys():
#  print(x)
