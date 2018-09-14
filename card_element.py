# encoding: utf-8

import curses
from colormap import ColorMap
from windows import initWindow


class CardElement(object):
    def __init__(self, suit, value, suit_color):
        self.suit = suit
        self.value = value
        self.suit_color = suit_color
