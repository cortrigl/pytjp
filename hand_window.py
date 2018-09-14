# encoding: utf-8

from colormap import ColorMap
from windows import initWindow


class HandWindow(object):
    def __init__(self, mh, mw):
        self.cmap = ColorMap()
        self.max_h = 9
        self.max_w = 41
        init_win = initWindow(self.max_h, self.max_w, self.cmap)
        self.hw_win = init_win.create(
            'handdisplay', 'blue_card', self.max_h, self.max_w)

    def draw_panel(self):
        bgcolor = self.cmap.colors['blue_card']
        self.hw_win.bkgd(bgcolor)

    def reset(self):
        self.hw_win.clear()
        self.draw_panel()
        self.hw_win.refresh()
