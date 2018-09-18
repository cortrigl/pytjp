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
            17: ('Four-of-a-kind', "FOUR-OF-A-KIND"),
            13: ('Full house', "FULL HOUSE"),
            11: ('Three-of-a-kind', "THREE-OF-A-KIND"),
            9: ('Two pair', "TWO PAIR"),
            7: 'One pair',
            5: ('Nothing', "NOTHING")
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
                    return ("Royal flush", "ROYAL FLUSH")
                return ("Straight flush", "STRAIGHT FLUSH")
            return ("Straight", "STRAIGHT")

        if self.is_same(suits):
            ''' Non-straight Flush '''
            return ("Flush", "FLUSH")
        total = sum([values.count(x) for x in values])
        if total == 7:
            for x in values:
                if values.count(x) > 1:
                    if x >= self.PAYOUT_HAND or x == 1:
                        return ("One pair", "HIGH PAIR")
                    else:
                        return ("Nothing", "LOW PAIR")

        return self.low_hands[total]

    def is_same(self, suit):
        return len(set(suit)) == 1

    def is_consecutive(self, values):
        return len(set(values)) == len(values) and \
            max(values) - min(values) == len(values) - 1


class Hand(object):
    def __init__(self):
        from card import Card
        self.hand = []
        self.card = Card()

    def deal_hand(self, new_deal=False):
        '''
        Draw cards and display them in the supplied curses container.

        Upon drawing the cards, call the evaluator to see what we have.
        '''
        from card_element import CardElement

        y = 6
        x = 3
        self.card.set_hand(self.hand)
        self.card.deal_cards(new_deal=new_deal)
        for c in range(len(self.hand)):
            self.card.get_symbol(self.hand[c][1])
            self.card.get_value(self.hand[c][0])
            self.card.get_suit_color(self.hand[c][1])

            curr_card = CardElement(
                y, x, self.card.symbol, self.card.value, self.card.suit_color)
            curr_card.reset()
            x += 10

        evalh = EvaluateHand(self.hand)
        result_hand = evalh.read_hand()

        return result_hand
