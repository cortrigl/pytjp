# encoding: utf-8

import sqlite3


class DataBase(object):
    def __init__(self):
        self._db = None

    def createDB(self):
        self._db = sqlite3.connect('tjp.db')
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

        self._db.cursor().execute('''
                                  CREATE TABLE system(
                                  id INTEGER PRIMARY KEY,
                                  num_royal_flush INT,
                                  num_straight_flush INT,
                                  num_four_of_a_kind INT,
                                  num_full_house INT,
                                  num_flush INT,
                                  num_straight INT,
                                  num_three_of_a_kind INT,
                                  num_two_pair INT,
                                  num_one_pair INT,
                                  num_games INT,
                                  num_distinct_users INT
                                  )
                                  ''')
        self._db.commit()


class UserData(object):
    def __init__(self):
        pass

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


class SystemData(object):
    def __init__(self):
        pass
