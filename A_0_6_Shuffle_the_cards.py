#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 27-01-2025
#A.0.6: Shuffle the cards!

import random

def createDeck():
    suit = ['s', 'h', 'd', 'c']         #  letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs.
    value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck=[] # creating an empty list inorder to add deck cards with type.
    for i in suit:  #
        for j in value:
            new_deck = i+j  # to create element for the deck e.g., s2,s3....
            deck.append(new_deck) # to add element to the list "deck".
          #  print(new_deck)
          #  print(deck)
    return deck
deck=createDeck() # calling createDeck()
new_deck=deck  # putting deck in new deck for shuffling
print("deck:",deck)
random.shuffle(new_deck) # randomly switches the positions of list new_deck elements.
print("shuffled deck1:",new_deck)
#print("shuffled deck2:",random.sample(deck,k=len(deck)))