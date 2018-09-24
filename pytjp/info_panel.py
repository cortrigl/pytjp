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
        # self.user_data.get_all('testerl')

    def draw_panel(self):
        self.user_data.get_all('testerl')
        plays_str = "Plays Left: {}".format(self.user_data.userdata['plays'])
        last_str = "Last Bet: {}".format(self.user_data.userdata['last_bet'])
        curr_str = "Current Bet: "
        cash_str = "Cash Left: {}".format(
            self.user_data.userdata['current_money'])
        str_color = self.cmap.colors['blue_stat']
        bgcolor = self.cmap.colors['white_stat']

        x = 2
        self.ip_win.bkgd(bgcolor)
        self.ip_win.addstr(3, x, plays_str, str_color)
        x += len(plays_str)
        self.ip_win.addstr(3, x + 6, cash_str, str_color)
        x = 2
        self.ip_win.addstr(9, x, last_str, str_color)
        x += len(last_str)
        self.ip_win.addstr(
            9, x, str(self.user_data.userdata['last_bet']), str_color)
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
        begin_str += self.mapping.indefinite_articles(hand_type.lower())
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
