from enum import Enum


class Color(Enum):
    HERZ = "♥"
    KARO = "◇"
    KREUZ = "†"
    PIK = "♤"


class CardValue(Enum):
    ZEHN = "10"
    BUBE = "B"
    DAME = "D"
    KOENIG = "K"
    ASS = "A"


class Card:
    def __init__(self, card_value: CardValue, color: Color):
        self.color = color
        self.value = card_value

    def __repr__(self):
        return str(self.color + self.value)

    def __eq__(self, other):
        return isinstance(other, Card) and self.value == other.value and self.color == other.color
