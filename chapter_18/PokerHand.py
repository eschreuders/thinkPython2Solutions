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
            if val == 2:
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
        print('rank numbers: ', ranknums)
        for i in range(len(ranknums)-1):
            if ranknums[i] == (ranknums[i+1]-1):
                count += 1
            elif ranknums[i] == (ranknums[i+1]):
                count += 0
            #ace can be number 14 if there's a king:
            elif ranknums[0] == 1 and ranknums[i+1] == 13:
                count += 1
            else:
                count = 0
            if count == 5:
                return True
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
            if val > 2 and not three:
                three = True
            if val > 2 and three:
                two = True
            if val == 2:
                two = True
        return two and three
        
    def has_fourofakind(self):
        """Returns True if the hand has four of a kind, False otherwise.
      
        """
        if not hasattr(self, 'ranks'):
            self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False 
        
    def has_straightflush(self):
        """Returns True if the hand has a straight, False otherwise.
      
        """
        count = 0
        ranknums = []
        for card in self.cards:
            ranknums.append(int(str(card.suit) + '{:02}'.format(card.rank)))
        ranknums = sorted(ranknums)
        print('Suit and rank numbers', ranknums)
        for i in range(len(ranknums)-1):
            if ranknums[i] == (ranknums[i+1]-1):
                count += 1
            elif ranknums[i] == (ranknums[i+1]):
                count += 0
            #ace can be number 14 if there's a king:
            elif ranknums[0] == 1 and ranknums[i+1] == 13:
                count += 1
            else:
                count = 0
            if count == 5:
                return True
        return False
        
if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print('Pair:            ', hand.has_pair())
        print('Two pair:        ', hand.has_twopair())
        print('Three of a kind: ', hand.has_threeofakind())
        print('Straight:        ', hand.has_straight())
        print('Flush:           ', hand.has_flush())
        print('Full house:      ', hand.has_fullhouse())
        print('Four of a kind:  ', hand.has_fourofakind())
        print('Straight flush:  ', hand.has_straightflush())
        print('')


