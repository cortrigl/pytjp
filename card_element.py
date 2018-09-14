# encoding: utf-8

import curses
from colormap import ColorMap
from windows import initWindow


class CardElement(object):
    def __init__(self, y, x, suit, value, suit_color, parent_win):
        self.suit = suit
        self.value = value
        self.suit_color = suit_color
        self.cmap = ColorMap()
        init_win = initWindow(None, None, self.cmap)
        self.ce_win = init_win.create(
            'card', 'white_card', None, None, parent_win, y, x)

    def draw_panel(self):
        pass
