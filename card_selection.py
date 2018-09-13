# encoding: utf-8

import curses
from colormap import ColorMap


class CardSelect(object):
    def __init__(self, win, hand=None):
        self.selected_cards = []
        self.cmap = ColorMap()
        self.hand = hand.hand
        self.win = win

    def main(self):
        '''
        main() is called after cards are dealt
        provides a loop to capture discard choices
        '''

        while True:
            c = self.win.getch()
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
        self.win.clear()
        self.selected_cards = []
        self.draw_card_selector()
        self.win.refresh()

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

        self.draw_card_selector()

    def draw_card_selector(self):
        '''
        Draw out the window that will contain the selector elements
        this needs to be separate from the card drawing.
        '''
        y = 0
        x = 5
        normal_color = self.cmap.colors['yellow_bg']
        select_color = self.cmap.colors['yellow_bg'] | curses.A_BOLD
        select_color |= normal_color
        card_numbers = [1, 2, 3, 4, 5]
        self.win.clear()
        for i in card_numbers:
            self.win.addstr(y, x, "(", self.cmap.colors['white_bg'])
            x += 1
            if i in self.selected_cards:
                self.win.addstr(y, x, str(i), select_color)
            else:
                self.win.addstr(y, x, str(i), normal_color)
            x += 1
            self.win.addstr(y, x, ")", self.cmap.colors['white_bg'])
            x += 9

        self.win.refresh()
