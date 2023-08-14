"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        print('Rank histogram: ', self.ranks)

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
        print('Suit histogram: ', self.suits)


    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
      
        """
        if not hasattr(self, 'ranks'):
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False        
    
    def has_twopair(self):
        """Returns True if the hand has two pair, False otherwise.
      
        """
        npair = 0
        if not hasattr(self, 'ranks'):
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                npair += 1
        if npair >= 2:
            return True
        return False    
        
    def has_threeofakind(self):
        """Returns True if the hand has three of a kind, False otherwise.
      
        """
        if not hasattr(self, 'ranks'):
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False 
        
    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.
      
        """
        count = 0
        ranknums = []
        for card in self.cards:
            ranknums.append(card.rank)
        ranknums = sorted(ranknums)
        if ranknums[0] == 1:
            ranknums.append(14)
        print('rank numbers: ', ranknums)
        for i in range(len(ranknums)-1):
            if ranknums[i] == (ranknums[i+1]-1):
                count += 1
            elif ranknums[i] == (ranknums[i+1]):
                count += 0
            else:
                count = 0
            if count == 4:
                return True
            print(i, count)
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        if not hasattr(self, 'suits'):
            self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
        
    def has_fullhouse(self):    
        """Returns True if the hand has a full house, False otherwise.      
        """ 
        three = False
        two = False
        if not hasattr(self, 'ranks'):
            self.rank_hist()
        for val in self.ranks.values():
            if val > 2 and three:
                two = True
            if val > 2 and not three:
                three = True
            if val == 2:
                two = True
        return two and three
        
    def has_fourofakind(self):
        """Returns True if the hand has four of a kind, False otherwise.
      
        """
        if not hasattr(self, 'ranks'):
            self.rank_hist()
        for val in self.ranks.values():
            if val == 4:
                return True
        return False 
        
    def has_straightflush(self):
        """Returns True if the hand has a straight, False otherwise.
      
        """
        count = 0
        ranknums = [[],[],[],[]]
        for card in self.cards:
            ranknums[card.suit].append(card.rank)
        for i in range(3):
            testing = ranknums[i]
            if len(testing) >= 5:
                count = 0
                testing = sorted(testing)
                print('Suit and rank numbers', testing)
                for i in range(len(testing)-1):
                    if testing[i] == (testing[i+1]-1):
                        count += 1
                    elif testing[i] == (testing[i+1]):
                        count += 0
                    else:
                        count = 0
                    if count == 4:
                        return True
                    print(i, count)
        return False
        
        
        
    def classify(self):
        self.label = 'nothing'
        if self.has_pair():
            self.label = 'pair'
        if self.has_twopair():
            self.label = 'two pair'
        if self.has_threeofakind():
            self.label = 'three of a kind'
        if self.has_straight():
            self.label = 'straight'
        if self.has_flush():
            self.label = 'flush'
        if self.has_fullhouse():
            self.label = 'full house'
        if self.has_fourofakind():
            self.label = 'four of a kind'
        if self.has_straightflush():
            self.label = 'straight flush'                                                
        
def deal_and_classify(ncard=5, nhand = 5):
    '''Creates a deck of cards, shuffles, hands out n hands and classifies
       Returns a dictionary of classifications and occurrences.      
    '''   
    pokerHands = {}
    deck = Deck()
    deck.shuffle()
    for i in range(nhand):
        hand = PokerHand()
        deck.move_cards(hand, ncard)
        hand.classify()
        pokerHands[hand.label] = pokerHands.get(hand.label, 0) + 1
    return pokerHands
        
def poker_sampling(nsamp=10, nhand = 5, ncard = 5):
    currentClassify      = {'nothing':0, 
                            'pair':0, 
                            'two pair':0, 
                            'three of a kind':0, 
                            'straight':0, 
                            'flush':0, 
                            'full house':0, 
                            'four of a kind':0, 
                            'straight flush':0}
    for i in range(nsamp):
        iteration = deal_and_classify(ncard, nhand)
        for key in iteration | currentClassify:
            currentClassify[key] = iteration.get(key,0) + currentClassify.get(key,0)
    print('')
    print('SAMPLING POKERHANDS')
    print('===================')
    print('sample size: {}    hands per deck: {}'.format(nhand * nsamp, nhand))
    print('===================')
    print('classification in numbers:')
    print(currentClassify)
    for key in currentClassify:
        currentClassify[key]= currentClassify[key] / (nhand*nsamp)            
    print('')
    print('classification ratio of {} samples:'.format(nhand * nsamp))
    print(print_dict(currentClassify))
    
def print_dict(diction):
    txt = []
    for key in diction:
        txt.append('{} : {:.3f}'.format(key, diction[key]))
    return '\n'.join(txt)
    
    
if __name__ == '__main__':
        
    print(poker_sampling(20000,5, 5))
            
            
         

