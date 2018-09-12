#!/usr/bin/env python3
# encoding: utf-8

import pygcurse


win = pygcurse.PygcurseWindow(40, 25, 'Allo allo')
win.pygprint('Allo!')
pygcurse.waitforkeypress()
