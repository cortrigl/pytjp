#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import sys
import curses

# local imports
import dropfile
from colormap import ColorMap
from hands import Hand
from card_selection import CardSelect
from info_panel import InfoPanel
from current_hand import CurrentHandPanel
from title_bar import TitleBar
from dropshadow import DropShadow
from hand_window import HandWindow
from database import UserData, SystemData


class Render(object):
    '''
    Initialize curses and display all the game window elements
    '''
    def __init__(self):
        self.ud = UserData()
        self.sd = SystemData()
        self.username = dropfile.process_dropfile("door.sys", "DOORSYS")
        self.ud.add(self.username)

        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.cmap = ColorMap()

    def main(self):
        '''
        Render.main()

        Start up the  curses main window and all subordinates. Then control
        the main menu loop.

        Basic notion is to instantiate the windows, then call their reset()
        method to display them.
        '''
        # The main curses screen
        self.stdscr.bkgd(self.cmap.colors['black_card'])
        self.stdscr.clear()
        self.stdscr.refresh()
        self.sd.get_plays()
        self.sd.get_games()
        self.ud.get_games(self.username)

        if self.ud.userdata['games'] == 0:
            # Out of plays for the day
            self.shutdown()

        # Start and initialize the various windows
        dropshadow = DropShadow(self.max_height, self.max_width)
        dropshadow.reset()
        info_bar = InfoPanel(self.max_height, self.max_width)
        info_bar.reset()
        card_disp = HandWindow(self.max_height, self.max_width)
        card_disp.reset()
        title = TitleBar(self.stdscr)
        title.reset()
        curr_hand = CurrentHandPanel(self.max_height, self.max_width)
        card_sel = CardSelect(self.max_height, self.max_width)

        # Start up a new Hand() object to obtain an empty hand array
        hand = Hand()

        '''
        The main menu loop. Refresh the dynamic elements - card selector,
        card display, and hand information windows.

        Then loop and wait for the various options
        '''
        while True:
            # Reset in a particular order to handle overlap
            info_bar.reset()
            curr_hand.main()
            card_disp.reset()
            card_sel.reset()

            c = self.stdscr.getch()
            if c == ord('q'):
                # quit was pressed, teardown and exit
                self.shutdown()
            elif c == ord('d') or c == ord('s'):
                '''
                Same bet or deal was pressed, deal a new round of cards,
                update the dynamic elements, and start the card selector
                loop. When the card selector returns, redeal for the
                discards then start again.
                '''
                self.ud.get_money(self.username)
                if self.ud.userdata['current_money'] == 0:
                    # out of money, try again next week
                    pass

                self.ud.get_plays(self.username)
                if self.ud.userdata['plays'] == 0:
                    # out of plays for this round
                    pass
                self.ud.set_plays(self.username,
                                  self.ud.userdata['plays'] - 1)
                # info_bar.reset()
                card_sel.draw_panel()
                ret = hand.deal_hand(new_deal=True)
                card_sel.set_hand(hand.hand)
                curr_hand.main(ret[0])
                card_sel.menu()

                ret = hand.deal_hand(new_deal=False)
                curr_hand.main(ret[0])
                info_bar.display_payoff(ret[1])
                hand.hand = []

                self.stdscr.getch()
            elif c == ord('e'):
                '''
                Enter new bet was pressed. Bring in the new bet dialog.
                '''
                pass
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
