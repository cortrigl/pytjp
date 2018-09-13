#!/usr/bin/env python3
# encoding: utf-8

import sys
import curses
from colormap import ColorMap
from hands import Hand
from card_selection import CardSelect
from info_panel import InfoPanel
from windows import initWindow
from current_hand import CurrentHandPanel
from title_bar import TitleBar
from dropshadow import DropShadow


class Render(object):
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.max_height, self.max_width = self.stdscr.getmaxyx()

    def main(self):
        self.cmap = ColorMap()
        self.stdscr.bkgd(self.cmap.colors['black_card'])
        self.stdscr.clear()
        self.stdscr.refresh()
        init_win = initWindow(self.max_height, self.max_width, self.cmap)
        dropshadow = DropShadow(self.max_height, self.max_width)
        dropshadow.reset()
        hs_win = init_win.create('handdisplay', 'blue_card')
        cs_win = init_win.create('cardselect', 'blue_card')
        ip_win = init_win.create('infopanel', 'blue_stat')
        ch_win = init_win.create('currenthand', 'blue_card')

        title = TitleBar(self.stdscr)
        card_disp = Hand(hs_win)
        # card_disp.reset()
        info_bar = InfoPanel(ip_win)
        curr_hand = CurrentHandPanel(ch_win)
        card_sel = CardSelect(cs_win, hand=card_disp)
        title.reset()

        while True:
            info_bar.main()
            curr_hand.main()
            card_disp.reset()
            card_sel.reset()

            c = self.stdscr.getch()
            if c == ord('q'):
                self.shutdown()
            elif c == ord('d'):
                # card_sel.reset()
                card_sel.draw_card_selector()
                ret = card_disp.deal_hand()
                curr_hand.main(ret[0])
                card_sel.menu(card_disp)

                ret = card_disp.deal_hand()
                curr_hand.main(ret[0])

                self.stdscr.getch()
            else:
                self.stdscr.addstr("Unrecognized key.")

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
