# encoding: utf-8

import sqlite3


class UserData(object):
    def __init__(self):
        self._db = sqlite3.connect('tjp_users.db')
        self._db.row_factory = sqlite3.Row

        self._db.cursor().execute('''
                                  CREATE TABLE user(
                                  id INTEGER PRIMARY KEY,
                                  name TEXT,
                                  bbs TEXT,
                                  sysop TEXT,
                                  last_bet INT,
                                  current_money INT,
                                  highest_money INT,
                                  best_hand TEXT,
                                  lw_money INT,
                                  lw_best_hand TEXT
                                  )
                                  ''')
        self._db.commit()

    def add(self, user):
        self._db.cursor().execute('''
                                  INSERT INTO user(id, name, bbs, sysop,
                                  last_bet, current_money, highest_money,
                                  best_hand, lw_money, lw_best_hand) VALUES(
                                  :id, :name, :bbs, :sysop, :last_bet,
                                  :current_money, :highest_money, :best_hand,
                                  :lw_money, :lw_best_hand)''', user)

    def get(self, user):
        self._db.cursor().execute("SELECT * FROM user WHERE id=:id",
                                  {'id': user}).fetchone()
