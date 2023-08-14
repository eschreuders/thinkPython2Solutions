import collections


#=======================
# In text exercises 19
#=======================
#original program
def uses_all(word, required):
    for letter in required: 
        if letter not in word:
            return False
    return True 
    
#generator fun

def uses_all_gen(word, required):
    return all(letter in word for letter in required)

    
# original program
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True 
    
#set exercise
def avoids_set(word, avoiding):
    return set(word) - set(avoiding) == set(word)

#original function
#def has_straightflush(self):
#    """Checks whether this hand has a straight flush.
#     Better algorithm (in the sense of being more demonstrably
#    correct).
#    """
#    # partition the hand by suit and check each
#    # sub-hand for a straight
#    d = defaultdict(list)
#    for c in self.cards:
#        d[c.suit].append(c.rank)#

    # see if any of the partitioned hands has a straight
#    for hand in d.values():
#        if len(hand.cards) < 5:
#            continue            
#        hand.make_histograms()
#        if hand.has_straight():
#            return True
#    return False

def binomial_coeff_ce(n,k):
    return 1 if k == 0 else 0 if n == 0 else binomial_coeff_ce(n-1, k) + binomial_coeff_ce(n-1, k-1)

     
if __name__ == "__main__":
    print(uses_all_gen("I love potatoes", "veto"))
    print(uses_all_gen("dreams", "door"))
    print(avoids_set("banana", "apple"))
    print(avoids_set("banana", "opple"))

    print(binomial_coeff_ce(4,2))
    
    
    

    
    
