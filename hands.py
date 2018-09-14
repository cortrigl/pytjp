# encoding: utf-8


class EvaluateHand(object):
    def __init__(self, hand):
        '''
        Need to work on exceptions for aces. They're being treated as
        low pairs and not part of a straight (or straight flush)
        '''
        self.PAYOUT_HAND = 10
        self.hand = hand
        self.low_hands = {
            17: ('Four-of-a-kind', "FOUR-OF-A-KIND!"),
            13: ('Full house', "A FULL HOUSE!"),
            11: ('Three-of-a-kind', "THREE-OF-A-KIND!"),
            9: ('Two pair', "TWO PAIR!"),
            7: 'One pair',
            5: ('Nothing', "NOTHING.")
        }

    def read_hand(self):
        suits = []
        values = []
        for (val, suit) in self.hand:
            suits.append(suit)
            values.append(val)

        if self.is_consecutive(values):
            ''' A straight '''
            if self.is_same(suits):
                ''' A straight flush '''
                if max(values) == 14:
                    ''' A royal flush '''
                    return ("Royal flush", "A ROYAL FLUSH!")
                return ("Straight flush", "A STRAIGHT FLUSH!")
            return ("Straight", "A STRAIGHT!")

        if self.is_same(suits):
            ''' Non-straight Flush '''
            return ("Flush", "A FLUSH!")
        total = sum([values.count(x) for x in values])
        if total == 7:
            for x in values:
                if values.count(x) > 1:
                    if x >= self.PAYOUT_HAND or x == 1:
                        return ("One pair", "A HIGH PAIR!")
                    else:
                        return ("Nothing", "A LOW PAIR.")

        return self.low_hands[total]

    def is_same(self, suit):
        return len(set(suit)) == 1

    def is_consecutive(self, values):
        return len(set(values)) == len(values) and \
            max(values) - min(values) == len(values) - 1


class Hand(object):
    def __init__(self, win):
        self.win = win
        self.hand = []
        self.new_deal = True

    def card_window(self):
        '''
        Construct the container that will hold the drawn cards.
        '''
        self.win.border()
        self.win.refresh()

    def reset(self):
        self.win.clear()
        self.hand = []
        self.new_deal = True
        self.card_window()

    def deal_hand(self):
        '''
        Draw cards and display them in the supplied curses container.

        Upon drawing the cards, call the evaluator to see what we have.
        '''
        from card import Card

        self.card = Card(hand=self)
        y = 1
        x = 2
        self.card.deal_cards(new_deal=self.new_deal)
        self.new_deal = False
        for c in range(len(self.hand)):
            self.card.render_card(self.win, y, x,
                                  self.hand[c][0],
                                  self.hand[c][1])
            x += 11

        self.win.refresh()

        evalh = EvaluateHand(self.hand)
        result_hand = evalh.read_hand()

        return result_hand
