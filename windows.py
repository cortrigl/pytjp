# encoding: utf-8
import curses


class initWindow(object):
    ''' Initialize a new curses window '''
    def __init__(self, max_h, max_w, cmap, y=None, x=None):
        self.max_h = max_h
        self.max_w = max_w
        self.cmap = cmap
        self.h = None
        self.w = None
        self.y = y
        self.x = x

    def create(self, w_name, color_name, h=None, w=None, pwin=None):
        self.h = h
        self.w = w
        bg_color = self.cmap.colors[color_name]
        (height, width, y, x) = self.setPosition(w_name)
        # if w_name == 'card':
        #    win = pwin.subwin(height, width, y, x)
        # else:
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
            'currenthand': chWindow,
            'titlebar': titleWindow,
            'titleline1': titleLineOne,
            'titleline2': titleLineTwo,
            'dropshadow': dsWindow,
            'cardslot': cardSlot,
            'card': cardElement
        }
        win_class = wins_to_positions[window_name](
            self.max_h, self.max_w, self.h, self.w, y=self.y, x=self.x)
        print("call to win class: {}; {}, {}, {}, {}, {}, {}".format(
            window_name, self.max_h, self.max_w,  self.h, self.w,
            self.y, self.x), file=open('/tmp/tjp.log', 'a'))
        return win_class.getWinSizePos()


class dsWindow(object):
    ''' Drop shadow window '''
    def __init__(self, mh, mw, h, wi, y=None, x=None):
        # height = mh - 4
        # width = mw - 3
        y = 3
        x = 1
        height = 22
        width = 77
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class csWindow(object):
    ''' Discard selection window '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        height = 1
        width = 51
        # y = mh - (height + 14)
        # x = mw // 2 - 30
        y = 4
        x = 2
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class hsWindow(object):
    ''' Card display window '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        height = 9
        width = 51
        y = 5
        x = 2
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class chWindow(object):
    ''' Type of current hand (full house, etc.) '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        height = 12
        width = 24
        # y = mh - (height + 20)
        # x = 2
        y = 4
        x = 53
        # x = mw // 2 - 30
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class ipWindow(object):
    ''' Information panel window '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        height = 10
        width = 75
        y = 13
        x = 2
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class titleWindow(object):
    '''  Title element '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        height = 2
        width = 46
        y = 0
        x = mw // 2 - 23
        self.window_data = (height, width, y, x)

    def getWinSizePos(self):
        return self.window_data


class titleLineOne(object):
    ''' First line of title '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        y = 0
        x = mw // 2 - (w // 2)
        self.window_data = (h, w, y, x)

    def getWinSizePos(self):
        return self.window_data


class titleLineTwo(object):
    ''' Second line of title '''
    def __init__(self, mh, mw, h, w, y=None, x=None):
        y = 1
        x = mw // 2 - (w // 2)
        self.window_data = (h, w, y, x)

    def getWinSizePos(self):
        return self.window_data


class cardSlot(object):
    def __init__(self, mh, mw, h, w, y=None, x=None):
        y = 0
        x = 0
        self.window_data = (h, w, y, x)

    def getWinSizePos(self):
        return self.window_data


class cardElement(object):
    def __init__(self, mh, mw, h, w, y=None, x=None):
        h = mh
        w = mw
        self.window_data = (h, w, y, x)

    def getWinSizePos(self):
        return self.window_data
