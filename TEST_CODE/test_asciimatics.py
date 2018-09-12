#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from asciimaticsi.widgets import (Frame, Text, Layout, ListBox, TextBox,
                                  Widget, Divider, Button)


class CardTable(Frame):
    def __init__(self, screen, model):
        super(CardTable, self).__init__(screen,
                                        screen.height
