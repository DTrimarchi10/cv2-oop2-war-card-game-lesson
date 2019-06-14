"""
Contains
- Rules
- Applies to players
- Deck changes happen here
"""

from player import Player
from deck import Deck


class War():
  def __init__(self,
               player1_name="Player1",
               player1_win_slogan="Great Game",
               player1_lose_slogan="Great Game",
               player2_name="Player2",
               player2_win_slogan="Great Game",
               player2_lose_slogan="Great Game"):
    self.player1 = Player(name=player1_name, win_slogan=player1_win_slogan, lose_slogan=player1_lose_slogan)
    self.player2 = Player(name=player2_name, win_slogan=player2_win_slogan, lose_slogan=player2_lose_slogan)
    self.deck = Deck()
    self.deal()
    self.middle_cards = []
    pass

  def deal(self):
    player1_hand = self.deck.cards[0::2]  #every other item in the deck list
    player2_hand = self.deck.cards[1::2]
    self.player1.hand = player1_hand
    self.player2.hand = player2_hand
    pass

  def play_round(self):
    p1_card = self.player1.draw_one()
    p2_card = self.player2.draw_one()
    self.add_to_middle([p1_card,p2_card])
    if p1_card > p2_card:
      self.player1.take_winnings(cards=self.middle_cards)
      print("Player 1 wins round")
    elif p2_card > p1_card:
      self.player2.take_winnings(cards=self.middle_cards)
      print("Player 2 wins round")
    else:
      self.play_war()

    self.reset_middle()
    pass

  def play_war(self):
    print("WAR!!!")
    p1_facedown = self.player1.draw_one()
    p1_facedown = self.player2.draw_one()
    self.add_to_middle([p1_facedown,p1_facedown])
    self.play_round()
    pass

  def add_to_middle(self, cards):
    self.middle_cards.extend(cards)
    pass

  def reset_middle(self):
    self.middle_cards = []
    pass

  def play_game(self):
    while len(self.player1.hand)>=1 and len(self.player2.hand)>=1:
      self.play_round()
    if self.player1.hand:
      print("{} Wins".format(self.player1.name))
    if self.player2.hand:
      print("{} Wins".format(self.player2.name))

if __name__=="__main__":
  war = War()
  print(war.deck.cards)
  print(war.player1.hand)
  print(war.player2.hand)
  war.play_game()

