#!/usr/bin/env python3
# encoding: utf-8

import sys
import curses
from colormap import ColorMap
from hands import Hand
from card_selection import CardSelect
from info_panel import InfoPanel
from current_hand import CurrentHandPanel
from title_bar import TitleBar
from dropshadow import DropShadow
from hand_window import HandWindow


class Render(object):
    '''
    Initialize curses and display all the game window elements
    '''
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.cmap = ColorMap()

    def main(self):
        self.stdscr.bkgd(self.cmap.colors['black_card'])
        self.stdscr.clear()
        self.stdscr.refresh()
        dropshadow = DropShadow(self.max_height, self.max_width)
        dropshadow.reset()
        info_bar = InfoPanel(self.max_height, self.max_width)
        info_bar.reset()
        card_disp = HandWindow(self.max_height, self.max_width)
        card_disp.reset()
        hand = Hand(card_disp)
        title = TitleBar(self.stdscr)
        title.reset()

        curr_hand = CurrentHandPanel(self.max_height, self.max_width)
        card_sel = CardSelect(self.max_height, self.max_width, hand=hand)

        while True:
            curr_hand.main()
            card_disp.reset()
            card_sel.reset()

            c = self.stdscr.getch()
            if c == ord('q'):
                self.shutdown()
            elif c == ord('d'):
                card_sel.draw_panel()
                ret = hand.deal_hand()
                curr_hand.main(ret[0])
                card_sel.menu(card_disp)

                ret = hand.deal_hand()
                curr_hand.main(ret[0])
                hand.hand = []

                self.stdscr.getch()
            else:
                pass

    def render_screen(self):
        self.main()

    @staticmethod
    def shutdown():
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        sys.exit()


if __name__ == '__main__':
    r = Render()
    r.render_screen()
    r.shutdown()
