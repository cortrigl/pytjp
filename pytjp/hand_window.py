# encoding: utf-8

from colormap import ColorMap
from windows import initWindow


class HandWindow(object):
    def __init__(self, mh, mw):
        self.cmap = ColorMap()
        h = mh
        w = mw
        init_win = initWindow(mh, mw, self.cmap)
        self.hw_win = init_win.create(
            'handdisplay', 'blue_card', h, w)

    def draw_panel(self):
        bgcolor = self.cmap.colors['blue_card']
        self.hw_win.bkgd(bgcolor)

    def reset(self):
        self.hw_win.clear()
        self.draw_panel()
        self.hw_win.refresh()
