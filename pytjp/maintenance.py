#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import os
from optparse import OptionParser

# local imports
import config
from database import StatsData, SystemData, UserData


def initial_maintenance():
    '''
    To be run on first installation.
    '''
    os.unlink('tjp.db')
    update_game_mechanics_from_config()

    return True


def update_game_mechanics_from_config():
    '''
    Obtain and use the game setup options from the ini file.
    '''
    # Pull the ini parameters and merge into a single dict
    (sysdata, gamedata) = config.init_pytjp_ini('settings.ini')
    # sysdata.update(gamedata)

    # Call the database handler to populate syatem data
    sd = SystemData()
    sd.add((sysdata, gamedata))

    # Now add a test user to the database
    ud = UserData()
    ud.add('testerl')

    return True


def monthly_maintenance():
    '''
    Update game settings based on ini file. This would be in case of
    tournaments or other changes to ini. This will also set the appropriate
    user fields (start money, plays, rounds, etc.)
    '''
    std = StatsData()
    std.get()

    return True


def weekly_maintenance():
    '''
    Reset weekly counters (user plays, last bet, current money,
    last week's best stats, etc.)
    '''
    return None


def daily_maintenance():
    '''
    Reset daily counters (user plays, number of rounds, yesterday's high hand)
    '''
    return None


def run_maintenance():
    '''
    Runs maintenance at the scheduled time, for the scheduled duration.

    Should run maintenance functions in ascending order of time length:
        - daily
        - weekly
        - monthly
    '''
    daily_maintenance()
    weekly_maintenance()
    monthly_maintenance()


if __name__ == '__main__':
    interval = None
    parser = OptionParser()
    parser.add_option(
        '-s', '--setup', action='store_true', dest='setup',
        help="Initialize database and prep for first run.")
    parser.add_option(
        '-w', '--weekly', action='store', dest='interval', default='weekly',
        help="Run weekly maintenance.")
    parser.add_option(
        '-m', '--montly', action='store', dest='interval', default='monthly',
        help="Run monthly maintenance")
    parser.add_option(
        '-d', '--daily', action='store', dest='interval', default='daily')

    (opts, args) = parser.parse_args()
    if opts.setup:
        initial_maintenance()
    elif opts.interval:
        if opts.interval == 'monthly':
            monthly_maintenance()
        elif opts.interval == 'weekly':
            weekly_maintenance()
        elif opts.interval == 'daily':
            daily_maintenance()
    else:
        run_maintenance()
