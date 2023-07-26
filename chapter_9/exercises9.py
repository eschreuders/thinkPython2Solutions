
#
# Exercise 9-1
#

fin = open("words.txt")
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)


#
# Exercise 9-2
#

print(bool)

def has_no_e(s):
    return 'e' in s

fin = open("words.txt")
countnoe = 0
count = 0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)
        countnoe = countnoe + 1
    count = count + 1

#print((countnoe/count)* 100,"% has no e")

#
# Exercise 9-2
#

def avoids(s, c):
    for letter in c:
        if letter in s:
            return False
    return True


def find_combo(string):
    fin = open("words.txt")
    countnoe = 0
    count = 0
    for line in fin:
        word = line.strip()
        if avoids(word, string):
            print(word)
            countnoe = countnoe + 1
        count = count + 1
    return (countnoe/count)* 100
    
print(find_combo("zxqjw"))


#
# Exercise 9-3
#


def find_percentage():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        fin = open("words.txt")
        countnoe = 0
        count = 0
        for line in fin:
            word = line.strip()
            if avoids(word, letter):
                countnoe = countnoe + 1
            count = count + 1
        perc = (countnoe/count)* 100
        if perc > 90:
            print(letter, "is not in: ", perc, "% of words")


#find_percentage()


#
# Exercise 9-4
#

def uses_only(word, string):
    word = word.replace(' ','')
    for letter in word:
        if letter not in string:
            return False
    return True
    
print(uses_only("towers","worstest"))
print(uses_only("towers","worst"))
print(uses_only("hello fool","acefhlo"))


#
# Exercise 9-5
#

def uses_all(word, string):
    word = word.replace(' ','')
    for letter in string:
        if letter not in word:
            return False
    return True


def find_combo_use(string):
    fin = open("words.txt")
    countnoe = 0
    count = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, string):
            print(word)
            countnoe = countnoe + 1
        count = count + 1
    return countnoe
    
print('aeiou', find_combo_use("aeiou"))
print('aeiouy', find_combo_use("aeiouy"))

#
# Exercise 9-6
#

def is_abecedarian(word):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        if letter not in abc:
            return False
        abc = letter + abc.partition(letter)[2]
    return True

def find_combo_abc():
    fin = open("words.txt")
    countnoe = 0
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            print(word)
            countnoe = countnoe + 1
        count = count + 1
    return countnoe        
        
print(find_combo_abc())


#
# Exercise 9-7
#

def cartalk(word):
    i = 0
    while len(word) >=6 and i < len(word) - 6:
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            return True
        i = i + 1
    return False
    
def find_cartalk():
    fin = open("words.txt")
    countnoe = 0
    count = 0
    for line in fin:
        word = line.strip()
        if cartalk(word):
            print(word)
            countnoe = countnoe + 1
        count = count + 1
    return countnoe        
        
print(find_cartalk())

#
# find_palindrome
#

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('1234'))

print(str(1234-1))

def cartalk2():
    for i in range(999996):
        test1 = str(i).zfill(6)[2:6]
        test2 = str(i+1).zfill(6)[1:6]
        test3 = str(i+2).zfill(6)[1:5]
        test4 = str(i+3).zfill(6)
        #print(str(i).zfill(6), test1, test2, test3, test4)
        if is_palindrome(test1) and is_palindrome(test2) and is_palindrome(test3) and is_palindrome(test4):
            print(i, "Is the magic number!")
            print(test1, test2, test3, test4)
         #   return True
    #return False

            
#print(cartalk2())

#
# Exercise Cartalk 3
#

def palindrome_age(age1, age2):
    diff = abs(age1 - age2)
    for i in range(150):
        sage1 = str(i)
        sage2 = str(i + diff)    
        sage3 = str(i + 1 + diff)
        sage4 = str(i + -1 + diff)
        if len(sage1) < len(sage2):
            sage1 = sage1.zfill(len(sage2))
        if sage1 == sage2[::-1] or sage1 == sage3[::-1] or sage1 == sage4[::-1]: 
            print("GOT ONE", sage1, sage2, sage3, sage4)
            
print(palindrome_age(37,73))

