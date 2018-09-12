#!/usr/bin/env python3

import curses

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, 2, 0)
    c = curses.color_pair(1)
    c |= curses.A_BOLD

    stdscr.addstr('c: {}'.format(c), c)
    stdscr.addstr('Again', curses.color_pair(1))

    stdscr.getch()

curses.wrapper(main)
