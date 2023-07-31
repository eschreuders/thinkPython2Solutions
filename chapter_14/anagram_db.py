import os
import time
import string
import shelve

from anagram_sets import all_anagrams, signature

def store_anagrams(anagram_dict, filename = 'anagrams.db'):
    '''Takes a dictionary of anagrams made with anagram_sets and stores it in
       a shelf.
       
       Uses:   anagram_sets
       input:  <anagram_dict> dictionary of <word>:<anagrams>
               <filename> name of the database.
       Output: shelf on disk in cwd named <filename>.
    '''
    s = shelve.open(filename)
    for word, anagrams in anagram_dict.items():
        print(word)
        s[word] = anagrams
    s.close()

def read_anagrams(word, databasename):
    '''Takes a word and checks a database of key:wordlist pairs for anagrams.
       
       uses:   anagram_sets
       input:  <word> string with word to check for anagrams.
               <databasename> filename string of database to open.
       output: list of strings with anagrams that go with <word>
    '''
    s = shelve.open(databasename)
    sign = signature(word)
    output = s[sign]
    s.close()
    return output

if __name__ == '__main__':
    anagram_map = all_anagrams("../words.txt")
    try:
        store_anagrams(anagram_map, 'anagrams.db')
    except:
        print("Could not store the anagram map.")
    try:
        print(read_anagrams('opts', 'anagrams.db'))
    except:
        print("Could not read the word.")
