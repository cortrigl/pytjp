# encoding: utf-8
import curses


class initWindow(object):
    ''' Initialize a new curses window '''
    def __init__(self, max_h, max_w, cmap):
        self.max_h = max_h
        self.max_w = max_w
        self.cmap = cmap

    def create(self, w_name, color_name):
        bg_color = self.cmap.colors[color_name]
        (height, width, y, x) = self.setPosition(w_name)
        win = curses.newwin(height, width, y, x)
        win.bkgd(bg_color)
        win.refresh()
        return win

    @property
    def getMaxHeight(self):
        return self.__max_h

    @getMaxHeight.setter
    def setMaxHeight(self, max_h):
        self.__max_h = max_h

    @property
    def getMaxWidth(self):
        return self.__max_w

    @getMaxWidth.setter
    def setMaxWidth(self, max_w):
        self.__max_w = max_w

    def setPosition(self, window_name):
        wins_to_positions = {
            'cardselect': csWindow,
            'handdisplay': hsWindow,
            'infopanel': ipWindow,
            'currenthand': chWindow
        }
        win_class = wins_to_positions[window_name](self.max_h, self.max_w)
        return win_class.getWinSizePos()


class csWindow(object):
    ''' Discard selection window '''
    def __init__(self, mh, mw):
        height = 1
        width = 60
        y = mh - (height + 14)
        x = mw // 2 - 30
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class hsWindow(object):
    ''' Card display window '''
    def __init__(self, mh, mw):
        height = 12
        width = 60
        y = mh - (height + 2)
        x = mw // 2 - 30
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class chWindow(object):
    ''' Type of current hand (full house, etc.) '''
    def __init__(self, mh, mw):
        height = 12
        width = 20
        y = mh - (height + 20)
        x = 2
        # x = mw // 2 - 30
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class ipWindow(object):
    ''' Information panel window '''
    def __init__(self, mh, mw):
        height = 1
        width = mw
        y = mh - height
        x = 0
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data
