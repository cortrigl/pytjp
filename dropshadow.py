# encoding: utf-8

import curses
from colormap import ColorMap
from windows import initWindow


class DropShadow(object):
    '''
    Simple class for drawing the grey matte behind the various
    game elements.
    '''
    def __init__(self, mh, mw):
        '''
        Takes in the max height and width from the main screen element
        '''
        self.cmap = ColorMap()
        init_win = initWindow(mh, mw, self.cmap)
        self.ds_win = init_win.create(
            'dropshadow', 'black_card', mh, mw)

    def draw_panel(self):
        bgcolor = curses.A_DIM
        bgcolor |= self.cmap.colors['white_card']
        self.ds_win.bkgd(bgcolor)

    def reset(self):
        self.ds_win.clear()
        self.draw_panel()
        self.ds_win.refresh()
