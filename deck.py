"""
This is going to be used to create a deck of cards for our game of war
"""

from random import shuffle

cards = list(range(1, 14))


class Deck():
  def __init__(self):
    self.cards = cards * 4
    shuffle(self.cards)    #shuffle method does in-place




# How can we test our code?
# if we run our file, it will run whatever we type
# in the 'if' statement below
if __name__=="__main__":
  mydeck = Deck()
  print("Created Deck Object, shuffling cards")
  print("here is your deck:")
  print(mydeck.cards)
  #Verify Deal
  print(mydeck.cards[0::2])
  print(mydeck.cards[1::2])