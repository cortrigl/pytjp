# encoding utf-8

from colormap import ColorMap
from windows import initWindow


class InfoPanel(object):
    '''
    White bg area for menu items and, money, and plays info
    '''
    def __init__(self, mh, mw):
        self.cmap = ColorMap()
        init_win = initWindow(mh, mw, self.cmap)
        self.ip_win = init_win.create('infopanel', 'black_card', mh, mw)

    def draw_panel(self):
        bgcolor = self.cmap.colors['white_stat']
        self.ip_win.bkgd(bgcolor)

    def reset(self):
        self.ip_win.clear()
        self.draw_panel()
        self.ip_win.refresh()
