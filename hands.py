# encoding: utf-8


class EvaluateHand(object):
    def __init__(self, hand):
        self.PAYOUT_HAND = 10
        self.hand = hand
        self.low_hands = {
            17: 'Four-of-a-kind',
            13: 'Full house',
            11: 'Three-of-a-kind',
            9: 'Two pair',
            7: 'One pair',
            5: 'Nothing'
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
                    return "Royal flush"
                return "Straight flush"
            return "Straight"

        if self.is_same(suits):
            ''' Non-straight Flush '''
            return "Flush"
        total = sum([values.count(x) for x in values])
        if total == 7:
            for x in values:
                if values.count(x) > 1:
                    if x > self.PAYOUT_HAND:
                        return "One pair"
                    else:
                        return "Nothing"

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

    def card_window(self):
        '''
        Construct the container that will hold the drawn cards.
        '''
        self.win.border()
        self.win.refresh()

    def deal_hand(self):
        '''
        Draw cards and display them in the supplied curses container.

        Upon drawing the cards, call the evaluator to see what we have.
        '''
        from card import Card

        self.card = Card(hand=self)
        y = 0
        x = 1
        self.card.deal_cards()
        for c in range(len(self.hand)):
            self.card.render_card(self.win, y, x,
                                  self.hand[c][0],
                                  self.hand[c][1])
            x += 11

        self.win.refresh()

        evalh = EvaluateHand(self.hand)
        result_hand = evalh.read_hand()

        return result_hand
