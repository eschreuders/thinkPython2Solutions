import os
import time
import string
import dbm 
import pickle
import hashlib




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
    pathlist = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filenm in filenames:
            pathlist.append(dirpath+'/'+filenm)
    return pathlist

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
        
################################
# Exercise 14-3
################################

def find_suffix(pathlist, suffix = '.exe'):
    '''Takes a list of pathnames and recursively searches for a given extension
       uses:   os
       Input:  parent directory
       Output: filenames with the correct extension
    '''
    rightsuffix = []
    for path in pathlist:
        splittie = [os.path.splitext(path)]
        for prefix, extension in splittie:
            if extension == suffix:
                rightsuffix.append(path)
    return rightsuffix

def filePairs(pathlist):
    '''Takes a list of pathnames and searches for double file names. Returns a
       list of path pair tuples. 
       Uses: os
       Input: <pathlist> list of paths to files you want checked.
       Output: list of <path>, <same filename> doubles.
    '''
    splitlist = [] 
    pairs = []
    for path in pathlist:
        splitlist.append(os.path.split(path))
    for i in range(len(splitlist)):
        for j in range(i+1,len(splitlist)):
            print(splitlist[i][1], splitlist[j][1])
            if splitlist[i][1] == splitlist[j][1]:
                pairs.append((splitlist[i][0]+'/'+splitlist[i][1],splitlist[j][0]+'/'+splitlist[j][1]))          
    return pairs

def comparemd5(pairlist):
    '''compares two files for equality.
       Input: list of file pairs (tuple)
       Output list of file p
    '''   
    for file1, file2 in pairlist:
        file1 = file1.replace(' ','\ ')
        file2 = file2.replace(' ','\ ')
        cmd1 = 'md5sum ' + file1
        cmd2 = 'md5sum ' + file2
        fp1 = os.popen(cmd1)
        res1 = fp1.read()
        stat1 = fp1.close()
        fp2 = os.popen(cmd2)
        res2 = fp2.read()
        stat2 = fp2.close()
        txt = "Are they the same? {result}!!!   ".format(result = res1.split()[0] == res2.split()[0])
        print(file1, file2)
        print(txt,res1.split()[0], res2.split()[0])

def comparediff(pairlist):
    '''compares two files for equality.
       Input: list of file pairs (tuple)
       Output list of file p
    '''   
    for file1, file2 in pairlist:
        file1 = file1.replace(' ','\ ')
        file2 = file2.replace(' ','\ ')
        cmd1 = 'diff ' + file1 + ' ' + file2
        fp1 = os.popen(cmd1)
        res1 = fp1.read()
        stat1 = fp1.close()
        print('differences for ',file1, file2)
        print(res1)


if __name__ == '__main__':

    ################################
    # Chapter 14, in-text exercises and playing
    ################################
    directory = '/home/esther/Nextcloud/Defolderwaarjeallesinhebtstaan/IT Treasury/pythonCourse/thinkpython'
    print(showFiles(directory))
    
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
    
    ################################
    # Chapter 14-1
    ################################
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
    
    ################################
    # Chapter 14-3, compage path names
    ################################
    allfiles = showFiles(directory)
    filestocheck = find_suffix(allfiles, '.py')
    filepairlist = filePairs(filestocheck)
    comparemd5(filepairlist)
    comparediff(filepairlist)
    
    
    
    
