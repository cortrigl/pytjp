# encoding: utf-8

import curses
from colormap import ColorMap
from windows import initWindow


class CardSelect(object):
    def __init__(self, mh, mw, hand=None):
        self.selected_cards = []
        self.cmap = ColorMap()
        self.max_h = 1
        self.max_w = 40
        init_win = initWindow(mh, mw, self.cmap)
        self.cs_win = init_win.create('cardselect', 'blue_card', mh, mw)
        self.hand = hand

    def set_hand(self, hand):
        self.hand = hand

    def menu(self):
        '''
        main() is called after cards are dealt
        provides a loop to capture discard choices
        '''
        while True:
            c = self.cs_win.getch()
            if c == ord('1'):
                self.select_card(1)
            elif c == ord('2'):
                self.select_card(2)
            elif c == ord('3'):
                self.select_card(3)
            elif c == ord('4'):
                self.select_card(4)
            elif c == ord('5'):
                self.select_card(5)
            elif c == curses.KEY_ENTER or c == 13 or c == 10:
                self.discard()
                break
            elif c == ord('q'):
                break
        return

    def reset(self):
        self.cs_win.clear()
        self.selected_cards = []
        # self.cs_win.border()
        self.draw_panel()
        self.cs_win.refresh()

    def discard(self):
        for c in reversed(self.selected_cards):
            v, s = self.hand.pop(c - 1)

    def select_card(self, card_number):
        '''
        select_card() puts selected discards into a list that
        will be correlated to the currently-held cards
        '''
        if card_number in self.selected_cards:
            self.selected_cards.remove(card_number)
        else:
            self.selected_cards.append(card_number)

        self.draw_panel()

    def draw_panel(self):
        '''
        Draw out the window that will contain the selector elements
        this needs to be separate from the card drawing.
        '''
        y = 0
        base_x = ((self.max_w - 1) // 5)
        offset = base_x - (base_x // 2)
        normal_color = self.cmap.colors['yellow_bg']
        select_color = self.cmap.colors['yellow_bg'] | curses.A_BOLD
        select_color |= normal_color
        card_numbers = [1, 2, 3, 4, 5]
        self.cs_win.clear()
        for i in card_numbers:
            x = (offset * i) + (offset * (i - 1))  # 4n + 4(n-1)
            if i in self.selected_cards:
                self.cs_win.addstr(y, x, str(i), select_color)
            else:
                self.cs_win.addstr(y, x, str(i), normal_color)
