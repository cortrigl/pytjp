# encoding: utf-8

import os.path
import sqlite3


class DataBase(object):
    def __init__(self):
        self._db = None
        db_name = 'tjp.db'
        self.connectDB(db_name)

    def connectDB(self, db_name):
        if not os.path.isfile(db_name):
            self.createDB(db_name)
        else:
            self._db = sqlite3.connect('tjp.db')
            self._db.row_factory = sqlite3.Row

    def createDB(self, db_name):
        self._db = sqlite3.connect(db_name)
        self._db.row_factory = sqlite3.Row

        self._db.cursor().execute('''
                                  CREATE TABLE user(
                                  id_num INTEGER PRIMARY KEY,
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
                                  id_num INTEGER PRIMARY KEY,
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


class UserData(DataBase):
    '''
    Handler for database operations on user accounts
    '''
    def __init__(self):
        self.userdata = None
        super(UserData, self).__init__()

    def add(self, user):
        '''
        Add a new user into the database
        :param user:
        '''
        data = {
            'id_num': 0,
            'name': user,
            'bbs': 'LanWarriors',
            'sysop': 'Anubis',
            'last_bet': 100,
            'current_money': 5000,
            'highest_money': 25000,
            'best_hand': "10D,11D,12D,13D,1D",
            'lw_money': 0,
            'lw_best_hand': ''
        }

        self._db.cursor().execute('''
                                  INSERT INTO user(id_num, name, bbs, sysop,
                                  last_bet, current_money, highest_money,
                                  best_hand, lw_money, lw_best_hand) VALUES(
                                  :id_num, :name, :bbs, :sysop, :last_bet,
                                  :current_money, :highest_money, :best_hand,
                                  :lw_money, :lw_best_hand)''', data)

    def get(self, user):
        self.userdata = self._db.cursor().execute(
            "SELECT * FROM user WHERE name=:name", {'name': user}).fetchone()


class SystemData(DataBase):
    def __init__(self):
        pass
