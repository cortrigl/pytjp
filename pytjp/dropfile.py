# -*- coding: utf-8 -*-
""" Read and parse the system dropfile """

# imports
import os


def open_file(dropfile):
    '''
    Open a dropfile and parse the contents into a list

    :param dropfile: The path to the dropfile
    '''

    data = []
    if not os.path.exists(dropfile):
        return False

    with open(dropfile, 'r') as df:
        for line in df:
            data.append(line)

    return data


def process_dropfile(dropfile, df_type):
    '''
    Pull out required information from a dropfile based on type

    :param dropfile: The path to the dropfile
    :param df_type: The variant of dropfile (DOOR.SYS, DORINFO, etc.)
    '''

    dropfile_data = open_file(dropfile)
    username = None

    # Currently we only need the username (will be used to key the database)
    if 'DOORSYS' in df_type:
        username = dropfile_data[9]
    elif 'DORINFO' in df_type:
        username = dropfile_data[6]
    elif 'CALLINFO' in df_type:
        username = dropfile_data[0]
    elif 'DOOR32' in df_type:
        username = dropfile_data[6]

    return username.rstrip()
