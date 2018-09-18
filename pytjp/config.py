# -*- coding: utf-8 -*-
""" Read and parse the system setting file """

# imports
import configparser

# local imports
from database import SystemData


def init_pytjp_ini(ini_file="settings.ini"):
    config = configparser.ConfigParser()
    config.read(ini_file)
    
    return (config['SYSTEM'], config['GAME'])
