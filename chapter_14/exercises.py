import os
import time
import string
import dbm 
import pickle
import anagram_sets




################################
# Chapter 14, in-text exercise
################################
def showFiles(directory = os.getcwd()):
    '''Take a given path, use os.walk to get all contents (dir and subdir).
       Print only the filenames. uses cwd if no path is given
       
       uses:   os module: walk() and getcwd() function
       input:  string with top directory path
       output: prints list of strings with parent directory and corresponding
               filenames
    '''
    for dirpath, dirnames, filenames in os.walk(directory):
        print([dirpath,filenames])

################################
# Exercise 14-1
################################
    
def sed(pattern, replacement, filein, fileout):
    '''Looks for pattern string in filein, replaces pattern occurence
       with the replacement string and saves in fileout.
       
       uses: os module, string module
       input: pattern string, replacement string two filename strings.
       output: file where pattern occurences have changed into replacement.
    '''
    
    try:
        fin = open(filein, 'r')
    except:
        print('could not open <filein> for reading')   
    
    try:
        fout = open(fileout, 'w')
    except:
        print('could not open <fileout> for writing')
    
    try:
        fileinlines = fin.readlines()
    except:
        print('Sorry, I cannot read from <fin>')  
        
    try:    
        for line in fileinlines:
            fout.write(line.replace(pattern, replacement))
    except:
        print('I can either not correctly replace the pattern or write to <fout>')    
    
    try:
        fin.close()
    except:
        print('cannot close <filein>')
        
    try:
        fout.close()
    except:
        print('cannot close <fileout>')

if __name__ == '__main__':

    ################################
    # Chapter 14, in-text exercises and playing
    ################################
    directory = '/home/esther/Nextcloud/Defolderwaarjeallesinhebtstaan/IT Treasury'
    showFiles(directory)
    
    #try dbm
    #db = dbm.open('captions','c')
    #db['cleese.png'] = 'Photo of John Cleese.' 
    #print(db['cleese.png'])
    #db.close
    
    #try pickling
    t = [1,2,'a cow']
    print(t)
    s = pickle.dumps(t)
    print(s)
    t2 = pickle.loads(s)
    print(t2)
    
    #try command line things
    cmd = 'ls -l'
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    print(res)
    print(stat)
    
    # E 14-1 try things that work and that raise an exception
    
    print('--- Should Work -------------------------------------')
    sed('i', 'CATS', 'fish.txt', 'apple.txt')    #works
    print('-----------------------------------------------------')
    print('--- Bad Filein --------------------------------------')
    sed('i', 'CATS', 'fish2.txt', 'apple.txt')   #filein doesn't exist\
    print('-----------------------------------------------------')
    print('--- Bogus pattern -----------------------------------')
    sed(2, 'CATS', 'fish.txt', 'apple.txt')    #pattern is bogus
    print('-----------------------------------------------------')
    print('--- Bogus Replacement -------------------------------')
    sed('i', 5, 'fish.txt', 'apple.txt')    #works
    print('-----------------------------------------------------')
    print('--- Bad Fileout -------------------------------------')
    sed('i', 'CATS', 'fish.txt', 3)    #fileout is bogus
    print('-----------------------------------------------------')

