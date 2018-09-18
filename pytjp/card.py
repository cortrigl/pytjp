# encoding: utf-8

from colormap import ColorMap
from deck import Deck


class Card(object):
    """ An individual card """
    def __init__(self, suit=None, value=None):
        self.cmap = ColorMap()
        self.blank_space = u'\u2588'
        self.heart = u'\u2665'
        self.club = u'\u2663'
        self.spade = u'\u2660'
        self.diamond = u'\u2666'
        # self.bg_color = curses.A_BOLD
        self.bg_color = self.cmap.colors['white_card']
        self.deck = Deck()
        self.deck.card_mapping()
        self.hand = None
        self.suit_color = None

    def set_hand(self, hand):
        self.hand = hand

    def get_symbol(self, suit):
        if suit == 'hearts':
            self.symbol = self.heart
        elif suit == 'diamonds':
            self.symbol = self.diamond
        elif suit == 'spades':
            self.symbol = self.spade
        elif suit == 'clubs':
            self.symbol = self.club

    def get_suit_color(self, suit):
        if suit == 'diamonds' or suit == 'hearts':
            self.suit_color = self.cmap.colors['red_stat']
        else:
            self.suit_color = self.cmap.colors['black_stat']

    def get_value(self, val):
        try:
            val = self.deck.face_cards[val]
        except KeyError:
            pass

        self.value = str(val)

    def deal_cards(self, new_deal=True):
        if new_deal:
            self.deck.new_deck()

        num_cards_to_deal = 5 - len(self.hand)
        for i in range(num_cards_to_deal):
            (val, suit) = self.deck.deck.pop()
            self.hand.append((val, suit))
