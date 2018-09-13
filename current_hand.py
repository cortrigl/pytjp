# encoding: utf-8

import curses
from colormap import ColorMap


class CurrentHandPanel(object):
    def __init__(self, win):
        self.cmap = ColorMap()
        self.win = win
        self.name_pos_map = {
            'Nothing': 1,
            'One pair': 2,
            'Two pair': 3,
            'Three-of-a-kind': 4,
            'Straight': 5,
            'Flush': 6,
            'Full house': 7,
            'Four-of-a-kind': 8,
            'Straight flush': 9,
            'Royal flush': 10
        }

    def main(self, hl_hand=None):
        print("in current_hand: {}".format(hl_hand),
              file=open('/tmp/tjp.log', 'a'))
        self.win.clear()
        self.draw_panel(hl_hand)
        self.win.refresh()

    def draw_panel(self, hand_to_highlight):
        x = 0
        hl_color = curses.A_BOLD
        hl_color |= self.cmap.colors['yellow_bg']
        normal_color = self.cmap.colors['white_bg']

        for key in self.name_pos_map.keys():
            if key == hand_to_highlight:
                self.win.addstr(self.name_pos_map[key], x, key, hl_color)
            else:
                self.win.addstr(self.name_pos_map[key], x, key, normal_color)
