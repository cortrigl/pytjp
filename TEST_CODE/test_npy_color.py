#!/usr/bin/env python3
# encoding: utf-8

import npyscreen
import curses


class syntaxTest(npyscreen.Textfield):
    def update_highlighting(self, start, end):
        print("start: {}, end: {}".format(start, end))
        hl_color = self.parent.theme_manager.findPair(self, 'WARNING')

        bold_green = curses.A_BOLD | curses.COLOR_GREEN
        self._highlightingdata = [
            bold_green,
            curses.A_BOLD,
            curses.A_BOLD,
            hl_color,
            hl_color,
            hl_color,
            hl_color,
            hl_color,
            hl_color,
            hl_color,
            hl_color,
            hl_color,
            hl_color
        ]


class themeManager(npyscreen.ThemeManager):
    # bold_green = curses.A_BOLD | curses.COLOR_GREEN
    # _colors_to_define = (
    #     ('BOLD_GREEN', int(bold_green), int(curses.COLOR_BLACK)))

    # print(
    #     "ctd: {}".format(_colors_to_define), file=open("/tmp/out.log", 'a'))
    def __init__(self):
        pass


class startForm(npyscreen.Form):
    def create(self):
        # bold_green = curses.A_BOLD | curses.COLOR_GREEN
        # tm = themeManager()
        # print(tm._defined_pairs, file=open("/tmp/out.log", "a"))
        bg = self.theme_manager.findPair(self, 'BOLDGREEN')

        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDMAGENTA',
                             relx=5, rely=8)
        self.test = self.add(npyscreen.FixedText, value='testing',
                             name="Test", editable=False, color='MAGENTA',
                             relx=5 + len('testing'), rely=8)

        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDBLUE',
                             relx=5, rely=9)
        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDGREEN',
                             relx=5, rely=10)
        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDWHITE',
                             relx=5, rely=11)
        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDRED',
                             relx=5, rely=12)
        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDYELLOW',
                             relx=5, rely=13)
        self.test = self.add(npyscreen.FixedText, value="testing",
                             name="Test", editable=False, color='BOLDCYAN',
                             relx=5, rely=14)
        # self.test.syntax_highlighting = True
        # self.test.highlight = True
        # self.test.color = 'BOLDGREEN'


class VideoP(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', startForm, name="Testing Bold")


videop = VideoP()
videop.run()
