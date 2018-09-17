# encoding utf-8

import curses
from colormap import ColorMap
from windows import initWindow
from mappings import Mappings
from database import UserData


class InfoPanel(object):
    '''
    White bg area for menu items and, money, and plays info
    '''
    def __init__(self, mh, mw):
        self.cmap = ColorMap()
        init_win = initWindow(mh, mw, self.cmap)
        self.ip_win = init_win.create('infopanel', 'black_card', mh, mw)
        self.mapping = Mappings()
        self.user_data = UserData()
        # self.user_data.add('testerl')
        self.user_data.get('testerl')


    def draw_panel(self):
        plays_str = "Plays Left: "
        last_str = "Last Bet: "
        curr_str = "Current Bet: "
        cash_str = "Cash Left: "
        str_color = self.cmap.colors['blue_stat']
        bgcolor = self.cmap.colors['white_stat']

        self.ip_win.bkgd(bgcolor)
        self.ip_win.addstr(3, 2, plays_str, str_color)
        self.ip_win.addstr(3, len(plays_str) + 6, cash_str, str_color)
        self.ip_win.addstr(9, 2, last_str, str_color)
        self.ip_win.addstr(
            9, 11, self.user_data.userdata['last_bet'], str_color)
        self.ip_win.addstr(9, 27, curr_str, str_color)

    def display_payoff(self, hand_type):
        y = 4
        x = 2
        curr_bet = 100
        payoff_amt = curr_bet * self.mapping.payoffs(hand_type.lower())
        payoff_str = "{:,}".format(payoff_amt)
        text_color = curses.A_BOLD
        text_color |= self.cmap.colors['white_stat']
        hl_color = self.cmap.colors['red_stat']
        begin_str = "You drew "
        if 'TWO' not in hand_type or 'ONE' not in hand_type \
                or 'THREE' not in hand_type or 'FOUR' not in hand_type:
            begin_str += "a "
        middle_str = "and it paid off "
        end_str = '!'
        self.ip_win.addstr(y, x, begin_str, text_color)
        x += len(begin_str)
        self.ip_win.addstr(y, x, hand_type, hl_color)
        x += (len(hand_type) + 1)
        self.ip_win.addstr(y, x, middle_str, text_color)
        x += len(middle_str)
        self.ip_win.addstr(y, x, '$', hl_color)
        x += len('$')
        self.ip_win.addstr(y, x, payoff_str, hl_color)
        x += len(payoff_str)
        self.ip_win.addstr(y, x, end_str, text_color)
        self.ip_win.refresh()

    def reset(self):
        self.ip_win.clear()
        self.draw_panel()
        self.ip_win.refresh()
