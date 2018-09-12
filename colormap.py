# encoding: utf-8
import curses


class ColorMap(object):
    def __init__(self):
        defined_colors = (('red', curses.COLOR_RED),
                          ('green', curses.COLOR_GREEN),
                          ('yellow', curses.COLOR_YELLOW),
                          ('blue', curses.COLOR_BLUE),
                          ('cyan', curses.COLOR_CYAN),
                          ('magenta', curses.COLOR_MAGENTA),
                          ('black', curses.COLOR_BLACK),
                          ('white', curses.COLOR_WHITE)
                          )

        self.colors = {}
        color_pair = 0

        for name, attr in defined_colors:
            color_pair += 1
            curses.init_pair(color_pair, attr, curses.COLOR_BLACK)
            self.colors[name] = curses.color_pair(color_pair)
            color_pair += 1
            curses.init_pair(color_pair, curses.COLOR_WHITE, attr)
            self.colors[name + '_card'] = curses.color_pair(color_pair)
            color_pair += 1
            curses.init_pair(color_pair, attr, curses.COLOR_BLUE)
            self.colors[name + '_bg'] = curses.color_pair(color_pair)
            color_pair += 1
            curses.init_pair(color_pair, attr, curses.COLOR_WHITE)
            self.colors[name + '_stat'] = curses.color_pair(color_pair)
