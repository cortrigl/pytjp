# encoding: utf-8

import curses
from colormap import ColorMap
from windows import initWindow


class TitleBar(object):
    def __init__(self, win):
        self.cmap = ColorMap()
        self.max_h, self.max_w = win.getmaxyx()
        init_win = initWindow(self.max_h, self.max_w, self.cmap)
        self.line1_win = init_win.create(
            'titleline1', 'black_card', h=1, w=17)
        self.line2_win = init_win.create(
            'titleline2', 'black_card', h=1, w=46)

    def draw_panel(self):
        '''
        Generates the title box to appear at the top of the game.

        TODO collect sysop and payoff from database/config
        '''
        sysop_color = curses.A_BOLD
        sysop_color |= self.cmap.colors['green']
        payoff_color = curses.A_BOLD
        payoff_color |= self.cmap.colors['red']
        line1_color = self.cmap.colors['cyan']
        line1_highlight = curses.A_BOLD
        line1_highlight |= line1_color
        line2_color = self.cmap.colors['white']

        sysop = 'ANUBIS'
        payoff = 'TENS'
        line2_middle_str = "has set the payoff to"

        y = 0
        x = 0
        self.line1_win.addstr(y, x, 'P', line1_highlight)
        x += 1
        self.line1_win.addstr(y, x, 'yTJ', line1_color)
        x += 4
        self.line1_win.addstr(y, x, 'V', line1_highlight)
        x += 1
        self.line1_win.addstr(y, x, 'ideo', line1_color)
        x += 5
        self.line1_win.addstr(y, x, 'P', line1_highlight)
        x += 1
        self.line1_win.addstr(y, x, 'oker', line1_color)

        y = 0
        x = 0
        self.line2_win.addstr(y, x, sysop, sysop_color)
        x += len(sysop) + 1
        self.line2_win.addstr(y, x, line2_middle_str, line2_color)
        x += len(line2_middle_str) + 1
        self.line2_win.addstr(y, x, payoff, payoff_color)
        x += len(payoff) + 1
        self.line2_win.addstr(y, x, "or better!", line2_color)

    def reset(self):
        self.line1_win.clear()
        self.line2_win.clear()
        self.draw_panel()
        self.line1_win.refresh()
        self.line2_win.refresh()
