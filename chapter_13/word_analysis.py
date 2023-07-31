from __future__ import print_function, division
import math
import random
import time
import string
import bisect

#
# Exercise 13-1 & 13-2
# Uniquewords/totalwords max goes to Corbett!



def extract_words(filepath, title, footer="*** end"):
    '''Returns a lowercase list of all words in a text file
       Reads the file, breaks lines into words, strips whitespace and 
       punctuation. Only reads lines from the title up to a designated footer 
       mark.
       
       filepath: path to the file to be extracted. 
       title: string, title of the book, used to skip headers, use no 
              uppercase! Transcribers notes may appear after "*** START", so
              we don't use the header
       footer: not required. string that marks the beginning of the footnote. 
               Use no uppercase! Standard: "*** end"      
       Returns: list of cleaned, lowercase words
    '''
    fin = open(filepath)
    wordlist = []
    space_replace = '' #needed for translation table
    past_header = False
    before_footer = True
    for i in range(0,len(string.whitespace)):
        space_replace = space_replace + ' '
    cleanwhite = str.maketrans(string.whitespace, space_replace)
    # concatenation added after comparing to wordlist (see EX13-4)
    cleanpunc = str.maketrans(' ',' ',string.punctuation + '”“’‘£' + string.digits)
    for line in fin:
        line = line.strip().lower()
        
        line = line.translate(cleanwhite) #replace all whitespace with spaces
        #check where line occurs in book
        if line.startswith(footer):
            before_footer = False
        if line.startswith(title):
            past_header = True
        line = line.translate(cleanpunc)  #remove punctuation
        if past_header and before_footer:
            line = line.split()               #split at space
            for word in line:
                wordlist.append(word)
    return wordlist
    
print(extract_words("1894_Corbett_The_adventures_of_dora_bell_detective.txt","the adventures of"))


books = (["1894_Corbett_The_adventures_of_dora_bell_detective.txt","the adventures of","W_1894_Corbett_The_adventures_of_dora_bell_detective.txt"], ["1871_Dundas_the_little_cap.txt","the little","W_1871_Dundas_the_little_cap.txt"],["1564_Shakespeare_Romeo_and_Juiliet.txt","the tragedy of romeo","W_1564_Shakespeare_Romeo_and_Juliet.txt"])

def extract_books():
    '''Takes a list of paths to texts and reads them, converts into a word list
       and writes to disk.
       
       inpaths: list of strings containing the paths to the texts to read.
       titles: titles of the texts, equal length to inpaths, used to skip header 
               info 
       outpaths: list of paths, equal length to inpaths, with paths to write to
       returns: set of files of books converted into lists of words.
    '''
    for book in books:
        print('at file: ', book[0])
        fout = open(book[2], 'w')     
        fout.write('\n'.join(extract_words(book[0],book[1])))
        fout.close()

def word_analysis(words):
    '''Takes a list of words (from a text or language for example)
       and counts the total amount of words, times each word is used and unique
       words.
       words: list of words
    '''
    data = dict()
    total = len(words) #total number of words in the book
    for word in words:
        if word not in data:
            data.update({word : [1,total,word]})
        else:
            data[word][0] = data[word][0] + 1
    unique = len(data) #total number of unique words in the book
    for uword in data:
        data[uword].append(unique)
        data[uword].append(data[uword][0]/data[uword][1]) #ratio of total word count
    return data
    
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

    
    
example = ["aapie","in",'aapie','twee','een','aapie','drie']
print("Cleaning Books!")
start_time = time.time()   
extract_books()
print(word_analysis(example))
#word_analysis(append_words("W_1564_Shakespeare_Romeo_and_Juliet.txt")))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")



#
# Exercise 13-3
#

def top_word_frequency(filename = "W_1564_Shakespeare_Romeo_and_Juliet.txt", topn = 20):
    '''Takes a list of words (from a text or language for example)
       and counts the times each word is used. Prints the top n
       words: list of words (default Romeo and Juliet)
       topn: size of the leading board to print (default 20)
       Returns: List of the most used words
    '''
    top = []
    wordcounts = sorted(word_analysis(append_words(filename)).values(),reverse=True)
    for i in range(0,topn):
        top.append(wordcounts[i][2])
    return top
    
    
print("Top 20!")
start_time = time.time()   
print('Romeo and Juiliet: ',top_word_frequency())
print('The Little Cap: ',top_word_frequency("W_1871_Dundas_the_little_cap.txt"))
print('Dora Bell: ',top_word_frequency("W_1894_Corbett_The_adventures_of_dora_bell_detective.txt"))


print("--- %s seconds ---" % (time.time() - start_time))
print("done!")

#
# Exercise 13-4
#
print("Read the English word list!")
start_time = time.time()   
wordlist = append_words()
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")


def word_compare(filename = "W_1564_Shakespeare_Romeo_and_Juliet.txt"):
    '''
    '''
    just_words = []
    words_in_book = sorted(word_analysis(append_words(filename)).values(),reverse=True)
    for i in range(0,len(words_in_book)):
        just_words.append(words_in_book[i][2])
    for word in just_words:
        if word not in wordlist:
            print(word)
            
print("Read the English word list!")
start_time = time.time()   
start_time = time.time()   
#print('Romeo and Juiliet: ',word_compare())
#print('The Little Cap: ',word_compare("W_1871_Dundas_the_little_cap.txt"))
#print('Dora Bell: ',word_compare("W_1894_Corbett_The_adventures_of_dora_bell_detective.txt"))
print("--- %s seconds ---" % (time.time() - start_time))
print("done!")
    
# lots of 'curly' apostrophes and quotes that aren't in the string.punctuation!
#recommend removing the curly apostrophes and the string "'s " during first cleanup.
#also took out digits and the british pound sign. 
#Measures should also be taken for contractions like 've 'll 's... 
#but, you know.. I'm done for now :)
print(string.punctuation)
         
         
#  
# 13-5
#
       
         
         
def histogram(s):
    '''Histogram function, taken from thinkpython2 text.
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d 

def choose_from_hist(d):    
    '''Takes a histogram dictionary and randomly picks a key.
       Odds are weighed by the histogram frequency
       d: dictionary {<key>:frequency}
       Returns: a key from the dictionary, pseudorandomly
    '''
    samplespace = []
    for key in d:
        samplespace.extend([key]*d[key])
    return random.choice(samplespace)
    
    
        
t = ['a', 'a', 'b']
hist = histogram(t)        
print(choose_from_hist(hist))


#  
# 19-Sets
#

#original solution chapter 9
def avoidsOriginal(s, c):
    for letter in c:
        if letter in s:
            return False
    return True

#new solution with sets

def avoids(s, c):
    '''Checks whether s and c have no characters in common using sets.
       s: first string to compare
       c: second string to compare
       returns: Boolean, True if there are no characters in commonm.
                Otherwise False
    '''
    return len(set(s) & set(c)) == 0
    
print(avoids('bear','cats')    )
print(avoids('beer','cats') )

#  
# 13-6
#

def word_compare_set(filename = "W_1564_Shakespeare_Romeo_and_Juliet.txt"):
    '''
    '''
    just_words = []
    words_in_book = set(append_words(filename))
    wordset = set(wordlist)
    print(words_in_book - wordset)
            
            
word_compare_set()


#
# 13-7
#bisect module

#
# Exercise 10-2
#

def word_histogram(words):
    '''Takes a list of words (from a text or language for example)
       and counts the total amount of words, times each word is used and unique
       words.
       words: list of words
    '''
    histogram = dict()
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram 

def cumsum(ulist):
    t = []
    for i in range(len(ulist)):
        t = t + [sum(ulist[0:i+1])]
    return t
    

def most_common(hist):
    '''Code partly borrowed from chapter 13 text. Turns dictionary of words and
       frequencies into a list of tuples, 
       Returns a list of frequency-word pairs
       hist: dictionary with words as keys and frequencies as values.       
    '''
    t = []
    for key, value in hist.items():\00s
        t.append((value, key))
    t.sort(reverse=True)
    return t
    
def cumulative_tuple(t):
    '''unzips and makes lists, calculates the cumulative sum and zips the words 
       and cumulative sum back together. Then returns a new list of tuples 
       because I need all the results...
       Uses: cumsum function
       t: list of tuples (frequency, word)
       Returns: list of sorted tuple cumsum-frequency pairs
    '''
    tlist = []
    unzipt = zip(*t)
    for tuples in unzipt:
        tlist.append(list(tuples))    
    cumulative = cumsum(tlist[0])
    return cumulative
    
    
def random_word_pick(filename = "W_1564_Shakespeare_Romeo_and_Juliet.txt"):    
    '''Takes a txt file with all the words from a book and picks one at random
       weighed by the frequency it appears in the text. 
       filename: name of the txt word file
       returns: the holy word, with frequency of appearance as a bonus.
    '''
    book_words = append_words(filename)
    book_hist = word_histogram(book_words)
    book_freq = most_common(book_hist)
    book_cumsum = cumulative_tuple(book_freq)
    n = len(book_words)
    rannumber = random.randint(0,n)    
    index = bisect.bisect(book_cumsum,rannumber)
    #some scaffolding to check whether this works:
    #print(rannumber)
    #print(index)
    #print('cumsum check ',book_cumsum[index])
    entry = book_freq[index]
    return entry
    
    
filename = "W_1564_Shakespeare_Romeo_and_Juliet.txt"    
  
    
print("Random word from Romeo and Juliet and number of appearances! ", random_word_pick())

