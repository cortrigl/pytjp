#!/usr/bin/env python3
# encoding: utf-8

import urwid


def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    else:
        txt.set_text(repr(key))


txt = urwid.Text(u"Allo le Monde")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)

loop.run()
