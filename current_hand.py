# encoding: utf-8

import curses
from colormap import ColorMap


class CurrentHandPanel(object):
    def __init__(self, win):
        self.cmap = ColorMap()
        self.win = win
        self.name_pos_map = {
            'Nothing': 0,
            'One pair': 1,
            'Two pair': 2,
            'Three-of-a-kind': 3,
            'Straight': 4,
            'Flush': 5,
            'Full house': 6,
            'Four-of-a-kind': 7,
            'Straight flush': 8,
            'Royal flush': 9
        }

    def main(self, hl_hand=None):
        self.win.clear()
        self.draw_panel(hl_hand)
        self.win.refresh()

    def draw_panel(self, hand_to_highlight):
        x = 0
        hl_color = curses.A_BOLD
        hl_color |= self.cmap.colors['yellow_bg']
        normal_color = self.cmap.colors['white_bg']

        for key in self.name_pos_map.keys():
            y = self.name_pos_map[key]
            x = 0
            self.win.addstr(y, x, '[', normal_color)
            x += 2
            self.win.addstr(y, x, ']', normal_color)
            x += 2
            if key == hand_to_highlight:
                self.win.addstr(y, x, key, hl_color)
                self.win.addstr(y, 1, u'\u2714', hl_color)
            else:
                self.win.addstr(y, x, key, normal_color)
