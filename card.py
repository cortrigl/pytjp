# encoding: utf-8

from colormap import ColorMap
from deck import Deck


class Card(object):
    """ An individual card """
    def __init__(self, suit=None, value=None, hand=None):
        self.cmap = ColorMap()
        self.blank_space = u'\u2588'
        self.heart = u'\u2665'
        self.club = u'\u2663'
        self.spade = u'\u2660'
        self.diamond = u'\u2666'
        # self.bg_color = curses.A_BOLD
        self.bg_color = self.cmap.colors['white_card']
        self.deck = Deck()
        self.deck.new_deck()
        self.deck.card_mapping()
        self.hand = hand.hand

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

    def render_card(self, win, y, x, val, suit):
        self.get_symbol(suit)
        self.get_suit_color(suit)
        self.get_value(val)

        (x_begin_1, x_begin_2, x_end_1, x_end_2) = (1, 8, 2, 9)
        if len(self.value) == 2:
            (x_begin_1, x_begin_2, x_end_1, x_end_2) = (1, 7, 3, 9)
        # win.addstr(y, x, self.blank_space * 10, self.bg_color)
        # y = y + 1
        win.addstr(y, x, self.blank_space, self.bg_color)
        win.addstr(y, x + x_begin_1, self.value, self.suit_color)
        win.addstr(y, x + x_end_1, self.blank_space * 6, self.bg_color)
        win.addstr(y, x + x_begin_2, self.value, self.suit_color)
        win.addstr(y, x + x_end_2, self.blank_space, self.bg_color)
        y = y + 1
        win.addstr(y, x, self.blank_space, self.bg_color)
        win.addstr(y, x + 1, self.symbol, self.suit_color)
        win.addstr(y, x + 2, self.blank_space * 6, self.bg_color)
        win.addstr(y, x + 8, self.symbol, self.suit_color)
        win.addstr(y, x + 9, self.blank_space, self.bg_color)
        for i in range(1, 4):
            y = y + 1
            win.addstr(y, x, self.blank_space * 10, self.bg_color)
        y = y + 1
        win.addstr(y, x, self.blank_space, self.bg_color)
        win.addstr(y, x + 1, self.symbol, self.suit_color)
        win.addstr(y, x + 2, self.blank_space * 6, self.bg_color)
        win.addstr(y, x + 8, self.symbol, self.suit_color)
        win.addstr(y, x + 9, self.blank_space, self.bg_color)
        y = y + 1
        win.addstr(y, x, self.blank_space, self.bg_color)
        win.addstr(y, x + x_begin_1, self.value, self.suit_color)
        win.addstr(y, x + x_end_1, self.blank_space * 6, self.bg_color)
        win.addstr(y, x + x_begin_2, self.value, self.suit_color)
        win.addstr(y, x + x_end_2, self.blank_space, self.bg_color)
        # y = y + 1
        # win.addstr(y, x, self.blank_space * 10, self.bg_color)

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
