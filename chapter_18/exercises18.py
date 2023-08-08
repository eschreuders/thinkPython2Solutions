import random

################################
# Chapter 18 Card games
################################

class Card:
    """Represents a standard playing card."""
    
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
        
    # Class attributes:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                  'Jack', 'Queen', 'King']
    
    def __str__(self):
        return '{} of {} '.format(Card.rank_names[self.rank], 
                                  Card.suit_names[self.suit])
                                  
    def __lt__(self, other):
        #check suits
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        return self.rank < other.rank
        
class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    def __str__(self):
        txt = []
        for card in self.cards:
            txt.append(str(card))
        return '\n'.join(txt)        

    def pop_card(self):
        return self.cards.pop() 

    def add_card(self, card):
        self.cards.append(card) 
        
    def shuffle(self):
        random.shuffle(self.cards) 

    def sort(self):
        self.cards.sort()
        
    def deal_hands(self, nhands = 1, ncards = 5):
        hands = []
        for i in range(nhands):
            hand = Hand()
            for j in range(ncards):
                hand.add_card(self.pop_card())
            hands.append(hand)
        return hands
        
class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label
         
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card()) 


#### Back to time!
                                  
class Time:
    def __init__(self, hour=0, minute=0, second =0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return '{:02.0f}:{:02.0f}:{:02.2f}'.format(self.hour, self.minute, self.second)
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds 

    def print_time(self):
        '''Takes a time object and prints it in format:
           hh:mm:ss
           Input: Time object
           Output: prints hh:mm:ss
        '''
        txt = '{:02.0f}:{:02.0f}:{:02.2f}'.format(timeobj.hour, timeobj.minute, timeobj.second)
        print(txt)

    def __lt__(self, other):
        ts = self.time_to_int()
        to = other.time_to_int()
        return ts < to   

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time    
        
def main():
    queen_of_diamonds = Card(1, 12)
    print(queen_of_diamonds)
    card1 = Card(2, 11)
    print(card1)
    
    print("Times again")
    time1 = Time(9, 30, 12)
    time2 = Time(1, 56, 33)
    
    print(time1, time2, time1 < time2)
    
    
    print('ON TO DECKS!!!')
    mydeck = Deck()
    print(mydeck)
    
    mydeck.shuffle()
    print(mydeck)
    
    mydeck.sort()
    print(mydeck)
    
    print('----\nLets deal some cards\n----')
    mydeck.shuffle()
    hands = mydeck.deal_hands(2, 4)
    for n in range(len(hands)):
        print('handno: {}'.format(n+1))
        print(hands[n])
    
if __name__ == "__main__":
    main()
    
    


