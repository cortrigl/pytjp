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


class Render(object):
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.max_height, self.max_width = self.stdscr.getmaxyx()

    def main(self):
        self.cmap = ColorMap()
        self.stdscr.bkgd(self.cmap.colors['blue_card'])
        self.stdscr.clear()
        self.stdscr.refresh()
        init_win = initWindow(self.max_height, self.max_width, self.cmap)
        hs_win = init_win.create('handdisplay', 'blue_card')
        cs_win = init_win.create('cardselect', 'blue_card')
        ip_win = init_win.create('infopanel', 'blue_stat')
        ch_win = init_win.create('currenthand', 'blue_card')

        hs = Hand(hs_win)
        ip = InfoPanel(ip_win)
        ch = CurrentHandPanel(ch_win)
        cs = CardSelect(cs_win, hand=hs)
        while True:
            ip.main()
            ch.main()
            cs.draw_card_selector()

            c = self.stdscr.getch()
            if c == ord('q'):
                self.shutdown()
            elif c == ord('d'):
                ret = hs.deal_hand()
                ch.main(ret)
                cs.main()
                hs.deal_hand()
                ch.main(ret)
                self.stdscr.getch()
            elif c == ord(' '):
                '''
                For testing purposes - this drains the deck after
                9 hits.
                '''
                hs.deal_hand(hs_win)
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
