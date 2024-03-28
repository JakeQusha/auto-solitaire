import hashlib
import json
from dataclasses import dataclass
from enum import Enum


class CardType(Enum):
    scam, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, T_THING, FULL = range(11)


class Card:
    type: CardType
    is_cheated: bool

    def __init__(self, card_type: CardType):
        self.type = card_type
        self.is_cheated = False


class Game:
    cards: list[list[Card]]
    last_card: CardType

    def add_card(self, card: Card, col: int):
        self.cards[col].append(card)

    def __init__(self):
        self.cards = [[] for _ in range(6)]
        self.last_card = CardType.SIX

    def __str__(self):
        return self.gethash() + '\n' + '\n'.join(
            [f"{i}: " + ' '.join([str(card.type)[9:] + (' C |' if card.is_cheated else ' |') for card in row]) for
             i, row in enumerate(self.cards)])

    # def __str__(self):
    #     return '\n'.join([f"{i}: "+' '.join([str(card.type)[9:]+(' C |' if card.is_cheated else ' |') for card in row]) for i,row in enumerate(self.cards)])

    def gethash(self):
        return ''.join(sorted([''.join(
            [str(card.type.value if card.type != CardType.FULL else 9) + ('19' if card.is_cheated else '') for card in
             row]) + ';' for row in self.cards]))


class Config:
    offset_right: int
    offset_left: int
    offset_top: int
    offset_bottom: int
    monitor_amount: int
    monitor_with_game: int

    def __init__(self, cfg_file: str):
        with open(cfg_file) as f:
            data = json.load(f)
            self.offset_top = data['offsets']['top']
            self.offset_bottom = data['offsets']['bottom']
            self.offset_left = data['offsets']['left']
            self.offset_right = data['offsets']['right']
            self.monitor_amount = data['monitor_amount']
            self.monitor_with_game = data['monitor_with_game']

    def __str__(self):
        return f'offset_top: {self.offset_top}, offset_bottom: {self.offset_bottom}, offset_left: {self.offset_left}, offset_right: {self.offset_right}, monitor_amount: {self.monitor_amount}, monitor_with_game: {self.monitor_with_game}'

    def get_corrected_offsets(self, width, height) -> tuple[int, int, int, int]:
        return (width / self.monitor_amount) * (self.monitor_with_game - 1) + self.offset_left, self.offset_top, (
                width / self.monitor_amount) * self.monitor_with_game - self.offset_right, height - self.offset_bottom
