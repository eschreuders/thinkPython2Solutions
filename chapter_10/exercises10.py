import math
import random
import time

#
# Exercise 10-1
#


def nested_sum(nestlist):
    nestsum = 0
    for i in nestlist:
        for j in i:
           nestsum += j
    return nestsum
    
    
t = [[1, 2], [3], [4, 5, 6]]
h = [[1], [3,9,1], [4, 5]]

print(nested_sum(t), ' is t total!')
print(nested_sum(h), ' is h total!')


#
# Exercise 10-2
#

def cumsum(ulist):
    t = []
    for i in range(len(ulist)):
        t = t + [sum(ulist[0:i+1])]
    return t
    
    
trala = [1,2,3,4]
print(cumsum(trala), ' cumulative total of trala! ',trala)

#
# Exercise 10-3
#

def middle(numlist):
    if (len(numlist) > 2):
        return numlist[1:-1]
    else:
        print("Sorry, there is no middle.")

test = [1,2,3,4,5,6,7,8,9]
print(middle(test),' the middle of ', test)
test2 = []
print(middle(test2),' the middle of ', test2)


#
# Exercise 10-4
#

def chop(somelist):
    """ Removes first and last element
        t: list
        Returns: None
    """
    del somelist[0]
    del somelist[-1]

t = [1,2,3,4,5]
chop(t)
print(t)


#
# Exercise 10-5
#

def is_sorted(mylist):
    """ Checks whether a list is sorted in ascending order
        mylist: list of characters or numbers
        Returns: True of False
    """
    for i in range(1,len(mylist)):
        print(mylist[i],' should be >= ',mylist[i-1])
        if mylist[i] < mylist[i-1]:
            return False
    return True

print(is_sorted([1,2,3]))
print(is_sorted(['b','a']))

#
# Exercise 10-6
#
        
def is_anagram(word1, word2):
    """Takes two strings and checks whether they are anagrams
       word1: string, first word to check
       word2: string, second word to compare to
       Returns: True or False
    """
    w1 = list(word1)
    w2 = list(word2)
    w1.sort()
    w2.sort()
    return w1 == w2
    
wordsy = "boon"
wordsy2 = "noob"
print(is_anagram("boon","noob"), " boon and noob are anagrams", wordsy, wordsy2)
print(is_anagram("cat","tack"), " cat and tack are anagrams")        

#
# Exercise 10-7
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
    
testseq = ("a","d","c")
testseq2 = ("a","d","a","c")
print(has_duplicates(testseq)," has duplicates and leaves the original alone", testseq)        
print(has_duplicates(testseq2)," has duplicates and leaves the original alone", testseq2)    


#
# Exercise 10-8
#

print(random.randint(1,366))

def gen_dates(num):
    """Generates num integers between 1 and 366 (representing day of year)
       feb 29th is left out because it's odds are not equal to the other 
       dates and I'm too lazy to account for it.
       num: an integer indicating size of the sample
       returns: a list of num random numbers representing days of year
    """
    t = []
    for i in range(num):
        t = t + [random.randint(1,366)]
    return t
    
print(gen_dates(10))


print(has_duplicates(gen_dates(10)))


def birthday_paradox(samplesize,numsamples):
    """Checks for duplicate birthdays within a given samplesize
       numsample times. A percentage of the amount of the positive testing 
       samples compared to the overal numsamples is returned.
       Uses: gen_dates, has_duplicates 
       
       samplesize: amount of people in the sample (class)
       numsamples: sample this many times to get an approximate chance.
       
       returns: ratio of positive duplicate samples and numsamples.
    """
    duplicates_found = 0
    for i in range(numsamples):
        if has_duplicates(gen_dates(samplesize)):
            duplicates_found += 1
    return duplicates_found / numsamples
    
print("odds of same birthdays in 23 size class: ", birthday_paradox(23,10000) )


#
# Exercise 10-9
#


def append_words():
    fin = open("words.txt")
    wordlist = []
    for line in fin:
        wordlist += [line.strip()]
    return wordlist
    
    
def append_words2():
    fin = open("words.txt")
    wordlist = []
    for line in fin:
        wordlist.append(line.strip())
    return wordlist
    
print("with the copy")
start_time = time.time()
append_words()
print("--- %s seconds ---" % (time.time() - start_time))
print("Done!")


print("without the copy")
start_time = time.time()
append_words2()
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


#
# Exercise 10-10
#


def in_bisect(mylist, word):
    ''' TROUBLE WITH RETURNS :) THAT'S WHY RECURSION DOESN'T WORK HERE
        Compares whether a given word appears before or after the middle of a 
        sorted list of words (alphabetically ascending). Then checks with the 
        half where the word should be until the word is found or the list 
        runs out and it isn't there. If the list has only two or less indices
        word is checked directly.
        
        mylist: A list of alphabetically ascending words
        word: the word you want to check for
        
        Returns: True if word is in mylist, false otherwise. 
    '''
    isthere = False
    print(len(mylist), word)
    if len(mylist) > 2:
        middle = int(len(mylist)/2)
        print(middle, " The middle index!")
        print(mylist[middle], " The middle word!")
        if mylist[middle] < word:
            in_bisect(mylist[middle : ], word)
            print("We're old")
        if mylist[middle] > word: 
            in_bisect(mylist[0 : middle], word)
            print("We're old")
        if mylist[middle] == word:
            print("It's true ", mylist[middle] == word)
            return True
    else:
        print(word in mylist, " is it in the list?")
        return word in mylist    


def in_bisect_for(mylist, word):
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
#        print(middle, " The middle index!")
#        print(mylist[middle], " The middle word!")
        if mylist[middle] < word:
            mylist = mylist[middle : ]
            length = len(mylist)
        elif mylist[middle] > word: 
            mylist = mylist[0 : middle]
            length = len(mylist)
        elif mylist[middle] == word:
            return True
    return word in mylist    



print("without the copy")
start_time = time.time()
beautifullist = append_words2()
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


print("bisection search")
start_time = time.time()
lala = in_bisect_for(beautifullist, "zest")
print("lala ", lala)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

print("word for word search")
start_time = time.time()
fala = "zest" in beautifullist
print("fala ", fala)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

#
# Exercise 10-11
#

def reverse_pair(wordlist):
    ''' Checks a word list for all the words that have a reverse friend in it.
        Makes sure not to double check by seeing if the word or reverse have 
        already been found.
    
        uses: bisection search 'in_bisect_for'
        wordlist: the list of words to be checked
        
        returns: friends, a list of all the words and theyr reverse
    '''
    friends = []
    for word in wordlist:
        reverse = word[::-1]
        if (word not in friends):
            if in_bisect_for(wordlist, reverse):
                friends = friends + [word, reverse]
    return friends


print("word for word search")
start_time = time.time()
#fala = reverse_pair(beautifullist)
#print(fala)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

#
# Exercise 10-12
#

def interlocked(wordlist, interval = 2):
    '''Finds all words in a list that have other words from that list 
       interlocked in them.
       (which means alternating letters form words of their own)
       
       uses: bisection search: in_bisect_for
       
       wordlist: list of words to be checked
       interval: number of words that will form a new one, standard is 2
       
       returns: the list of words that are this way and the words they're made up of
    '''
    interlockers = []   
    for word in wordlist:
        searchwords = []
        check = True
        for i in range(interval):
            searchwords = searchwords + [word[i::interval]] 
        #print(searchwords)
        for searchword in searchwords:
            if not in_bisect_for(wordlist,searchword):
                check = False
                break
        if check:
            interlockers += [word, searchwords]
    return interlockers


print("Interlocking words interval 3")
start_time = time.time()
fala = interlocked(beautifullist,3)
print(fala)
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")
            
            
            
    



