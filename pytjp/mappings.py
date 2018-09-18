# encoding: utf-8


class Mappings(object):
    def __init__(self):
        pass

    @staticmethod
    def payoffs(hand_type):
        payoff_amounts = {
            'royal flush': 500,
            'straight flush': 300,
            'four-of-a-kind': 200,
            'full house': 100,
            'flush': 50,
            'straight': 25,
            'three-of-a-kind': 15,
            'two pair': 5,
            'high pair': 1,
            'low pair': 0,
            'nothing': 0
          }

        return payoff_amounts[hand_type]

    @staticmethod
    def indefinite_articles(hand_type):
        articles = {
            'royal flush': 'a ',
            'straight flush': 'a ',
            'four-of-a-kind': ' ',
            'full house': 'a ',
            'flush': 'a ',
            'straight': 'a ',
            'three-of-a-kind': ' ',
            'two pair': ' ',
            'high pair': 'a ',
            'low pair': 'a ',
            'nothing': ' '
        }

        return articles[hand_type]
