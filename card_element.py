# encoding: utf-8

from colormap import ColorMap
from windows import initWindow


class CardElement(object):
    def __init__(self, y, x, suit, value, suit_color):
        self.suit = suit
        self.value = value
        self.suit_color = suit_color
        self.cmap = ColorMap()
        init_win = initWindow(7, 9, self.cmap, y, x)
        self.ce_win = init_win.create('card', 'white_card')

    def draw_panel(self):
        '''
        draw_panel():

        Render the card as a curses subwindow

        TODO: add symbols to middle of the card
        '''
        #  set the positioning of the card face text
        top_value_x = 1
        top_suit_x = 1 + len(str(self.value))
        bottom_suit_x = 7
        if len(str(self.value)) > 1:
            bottom_value_x = 7 - (len(str(self.suit)) + 1)
        else:
            bottom_value_x = 7 - len(str(self.suit))
        top_y = 0
        bottom_y = 6

        self.ce_win.addstr(
            top_y, top_value_x, str(self.value), self.suit_color)
        self.ce_win.addstr(top_y, top_suit_x, self.suit, self.suit_color)
        self.ce_win.addstr(
            bottom_y, bottom_value_x, str(self.value), self.suit_color)
        self.ce_win.addstr(bottom_y, bottom_suit_x, self.suit, self.suit_color)

    def reset(self):
        self.ce_win.clear()
        self.draw_panel()
        self.ce_win.refresh()
