# encoding: utf-8

import random
import itertools


class Deck(object):
    ''' Deck of cards class '''
    def __init__(self):
        self.deck = list(itertools.product(
            range(1, 14), ['spades', 'hearts', 'diamonds', 'clubs']))
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def card_mapping(self):
        self.face_cards = {}
        self.face_cards[1] = 'A'
        self.face_cards[11] = 'J'
        self.face_cards[12] = 'Q'
        self.face_cards[13] = 'K'
