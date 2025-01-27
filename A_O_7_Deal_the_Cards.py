#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 27-01-2025
#A.0.7: Deal the cards!

import random

class Cards:
    def __init__(self):
        self.cards = []
    def create(self):
        self.cards=[]
        suit = ['s', 'h', 'd', 'c']  #  letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs
        value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for suits in suit:
            for rank in value:
                new_deck=suits+rank
                self.cards.append(new_deck)
        return self.cards



    def shuffle (self):
        random.shuffle(self.cards)



    def deal(self, num_of_hands, cards_per_hand):
        hand_list = [[] for i in range(num_of_hands)] # creating empty deck (array of arrays) to store cards distributed to each hand.
        for i in range(cards_per_hand):  # loop to distribute cards per hand.
            for hand in hand_list:  # loop to distribute cards to players in sequence from deck.
                if self.cards:
                    hand.append(self.cards.pop(0)) # this will pop out each element from cards deck to hand_list.
            #print(hand_list)
        return hand_list


card_01 = Cards() # initializing the class with object card_01
card_01.create()  # calling the create function using object to create the deck.
print(card_01.cards)
card_01.shuffle()  # calling the shuffle function to shuffle the deck.
print(card_01.cards)
hand_list = card_01.deal(5, 10)  # Calling deal function to distribute cards to the players into hand_list array.
print(hand_list)
print("Remaining deck:", card_01.cards)