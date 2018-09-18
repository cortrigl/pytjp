# encoding: utf-8

import os.path
import sqlite3


class DataBase(object):
    """
    SQLLite3 connection and query operations
    """
    def __init__(self):
        self._db = None
        db_name = 'tjp.db'
        self.connectDB(db_name)

    def connectDB(self, db_name):
        """
        Attempt a datbase connection

        :param db_name str: The database file to which to connect
        """

        # If the database doesn't exist, create and connect
        if not os.path.isfile(db_name):
            self.createDB(db_name)
        else:
            self._db = sqlite3.connect('tjp.db')
            self._db.row_factory = sqlite3.Row

    def createDB(self, db_name):
        """
        Connect and build sqlite3 table structures

        :param db_name str: The database file to which to connect
        """
        self._db = sqlite3.connect(db_name)
        self._db.row_factory = sqlite3.Row

        # Create the user table
        self._db.cursor().execute('''
                                  CREATE TABLE user(
                                  id_num INTEGER PRIMARY KEY,
                                  name TEXT,
                                  games INT,
                                  plays INT,
                                  last_bet INT,
                                  current_money INT,
                                  highest_money INT,
                                  best_hand TEXT,
                                  lw_money INT,
                                  lw_best_hand TEXT
                                  )
                                  ''')
        self._db.commit()

        # Create the system table
        self._db.cursor().execute('''
                                  CREATE TABLE system(
                                  id_num INTEGER,
                                  bbs TEXT,
                                  sysop TEXT,
                                  low_hand INT,
                                  plays INT,
                                  games INT,
                                  start_money INT
                                  ''')
        self._db.commit()

        # Create the statistics table
        self._db.cursor().execute('''
                                  CREATE TABLE stats(
                                  id_num INTEGER,
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
        # One extra step for stats - create a row with all zeroes
        self._db.cursor().execute(
            '''INSERT INTO stats(id_num, num_royal_flush, num_straight_flush,
            num_four_of_a_kind, num_full_house, num_flush, num_straight,
            num_three_of_a_kind, num_two_pair, num_one_pair, num_games,
            num_distinct_users) VALUES(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)''')
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
        Add a new user into the database. Should be triggered on encounter
        with an unknown username

        :param user:
        '''

        # Pull the default system parameters (cash, num plays, etc.)
        sysdata = SystemData()
        data = sysdata.get()

        self._db.cursor().execute("""INSERT INTO user(name, games, plays,
                                  last_bet, current_money, highest_money,
                                  best_hand, lw_money, lw_best_hand) VALUES(
                                  '{}', {}, {}, 0, 0, 0, '', 0, '')""".format(
                                      user, data['games'], data['games']))
        self._db.commit()

    def get_all(self, user):
        '''
        Obtain all data for the supplied user name
        :param user:
        '''
        self.userdata = self._db.cursor().execute(
            "SELECT * FROM user WHERE name=:name", {'name': user}).fetchone()

        if len(self.userdata.keys()) == 0:
            self.add(user)

        self.userdata = self._db.cursor().execute(
            "SELECT * FROM user WHERE name=:name", {'name': user}).fetchone()

    def set(self, query):
        '''
        Update a user  entry
        :param query:
        '''
        self._db.cursor().execute(query)
        self._db.commit()

    def get(self, query):
        self.userdata = self._db.cursor().execute(query).fetchone()

    def get_plays(self, user):
        """
        Retrieve number of plays left
        :param user str: Username to search for in DB
        """
        self.get("SELECT plays FROM user WHERE user='{}'".format(user))

    def get_games(self, user):
        """
        Retrieve number of games left
        :param user str: Username to search for in DB
        """
        self.get("SELECT games FROM user WHERE user='{}'".format(user))


class SystemData(DataBase):
    """
    Handler for database operations on system information
    """
    def __init__(self):
        self.sysdata = None
        super(SystemData, self).__init__()

    def add(self, (sys_dict, game_dict)):
        """
        Add system data to the database

        :param dict sys_dict: Basic system information
        :param dict game_dict: Various game settings
        """

        data = sys_dict
        data.update(game_dict)

        # First check if the system table has an entry
        sth = self.get()
        if len(sth.keys) == 0:
            # Insert query
            self._db.cursor().execute(
                '''INSERT INTO system(id_num, bbs, sysop, low_hand, plays,
                games, start_money) VALUES(0, :bbs, :sysop, :low_hand,
                :plays, :games, :start_money)''', data)
        else:
            # Update query
            self._db.cursor().execute(
                '''UPDATE system SET bbs=':bbs',sysop=':sysop',
                low_hand=':low_hand', plays=:plays, games=:games,
                start_money=:start_money WHERE id_num = 0''', data)
        self._db.commit()

    def get_all(self):
        self.sysdata = self._db.cursor.execute(
            "SELECT * FROM system where id_num = 0").fetchone()

    def get(self, query):
        self.sysdata = self._db.cursor.execute(query).fetchone()

    def set(self, query):
        """
        Update the system entry
        :param query str: The SQL query to directly execute
        """
        self._db.cursor().execute(query)
        self._db.commit()

    def get_plays(self):
        """
        Retrieve max number of plays
        """
        self.get("SELECT plays FROM system")

    def get_games(self):
        """
        Retrieve max number of games
        """
        self.get("SELECT games FROM system")


class StatsData(DataBase):
    """
    Handler for the system/games statistics
    """
    def __init__(self):
        self.statsdata = None
        super(StatsData, self).__init__()

    def get(self):
        """
        Retrieve stats data
        """
        self.sysdata = self._db.cursor().execute(
            "SELECT * FROM stats where id_num = 0").fetchone()

    def set(self, params):
        """
        Update the stats

        :param params dict: The key/val pairs describing what to update
        """
        for key in params.keys():
            self._db.cursor().execute(
                '''UPDATE stats SET {} = ? WHERE id_num = 0'''.format(key),
                params[key])
            self._db.commit()
