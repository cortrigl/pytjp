#!/usr/bin/env python2
# encoding: utf-8

import npyscreen
import curses


class syntaxTest(npyscreen.Textfield):
    def __init__(self, *args, **kwargs):
        self.end = kwargs.pop('end_str')
        super(syntaxTest, self).__init__(
            highlight_whole_widget=True,
            hightlight_color='IMPORTANT',
            invert_highlight_color=False, *args, **kwargs)

    def update_highlighting(self, start, end):
        hl_color = self.parent.theme_manager.findPair(self, 'IMPORTANT')
        hl_colorb = self.parent.theme_manager.findPair(self, 'WARNING')
        hl_colorc = self.parent.theme_manager.findPair(self, 'CRITICAL')

        self._highlightingdata = [curses.A_BOLD | curses.COLOR_GREEN,
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


class startForm(npyscreen.Form):
    def __init__(self, *args, **kwargs):
        '''
        bbsname, user, sysop, etc. passed in via kwargs...
        Same deal, we need to get at ther super's __init__ for stuff
        like self.parentApp and such
        '''
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.sysop = kwargs.pop('sysop')
        self.user = kwargs.pop('username')
        self.bbs = kwargs.pop('bbsname')
        self.db_get_user_info()
        self.db_get_system_info()
        super(startForm, self).__init__(*args, **kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def db_get_system_info(self):
        '''
        Get the system configuration and stored data from sqlite
        '''
        self.lowest_hand = 'tens'
        self.best_hand_week = ''
        self.best_hand_user_week = ''
        self.most_money_week = '100,000'
        self.most_money_user_week = 'mikey'

    def db_get_user_info(self):
        '''
        Get the user info (remaining money, bonus, best hand, last bet, etc.)
        from the sqlite db.
        '''
        self.current_money = 1000
        self.last_bet = 10
        self.current_bet = 10

    def create(self):
        self.db_get_user_info()
        payout_val = "Sysop ({}) has set the payout to ".format(self.sysop)
        stuff = "{} or better.".format(self.sysop, self.lowest_hand)
        currmon_val = "Current money: ${}".format(self.current_money)
        lastbet_val = "Last wager: ${}".format(self.last_bet)

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        color = curses.A_BOLD
        color |= curses.color_pair(1)

        self.min_text = self.add(
            syntaxTest, editable=False, end_str=len(payout_val),
            value=payout_val, relx=-1 * (len(payout_val) + 5), rely=2)
        self.min_text.syntax_highlighting = True

        self.cm_text = self.add(
            syntaxTest, color='CYAN_BLACK', syntax_highlighting=True,
            end_str=len(currmon_val), value=currmon_val, relx=3, rely=5)
        self.cm_text.syntax_highlighting = True
        self.lb_text = self.add(
            npyscreen.FixedText,
            value=lastbet_val, relx=3)
        # self.display()


class VideoP(npyscreen.NPSAppManaged):
    def __init__(self, *args, **kwargs):
        '''
        Passing in everything via kwargs then removing them from the dict.
        This way, we can continue with loading the super's __init__
        In theory this will all be done through a dropfile, but I've not
        yet looked into how x84 handles native python doors.
        '''
        self.bbs = kwargs.pop('bbsname')
        self.user = kwargs.pop('username')
        self.sysop = kwargs.pop('sysop')
        super(VideoP, self).__init__(*args, **kwargs)

    def onStart(self):
        self.addForm('MAIN', startForm,
                     name="{} presents Python Video Poker".format(self.bbs),
                     username=self.user, sysop=self.sysop, bbsname=self.bbs)


class readDropFile(object):
    def __init__(self, file_path):
        '''
        Open, parse, and recover values from the x84 drop file.
        This is currently an unknown as I do not know if x84 drops for
        a native (python) door or if it's launched directly from sesame or
        door.py.
        '''
        self.file_path = file_path

    def open_drop_file(self):
        pass

    def parse_drop_file(self):
        pass

    def get_username(self):
        pass

    def get_sysop(self):
        pass

    def get_bbs(self):
        pass


class dbGetData(object):
    def __init__(self, db_file):
        '''
        Open and read values in SQLite based on the user. Looking for
        such fields as user's current cash, their last bet amount, etc.
        '''
        self.db_file = db_file

    def db_open(self):
        pass

    def get_user_info(self):
        pass


if __name__ == '__main__':
    videop = VideoP(bbsname="Mega Lo Mart",
                    username='testerl',
                    sysop='jimmy').run()
