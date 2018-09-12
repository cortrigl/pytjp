# encoding utf-8

import curses
from colormap import ColorMap


class InfoPanel(object):
    def __init__(self, win):
        self.cmap = ColorMap()
        self.win = win

    def main(self):
        self.draw_info_panel()
        self.win.refresh()

    def draw_info_panel(self):
        y = 0
        x = 1
        hl_color = curses.A_BOLD
        hl_color |= self.cmap.colors['yellow_stat']

        self.win.addstr(y, x, '(')
        x += 1
        self.win.addstr(y, x, 'Q', hl_color)
        x += 1
        self.win.addstr(y, x, ')')
        x += 2
        self.win.addstr(y, x, 'exit to BBS')
