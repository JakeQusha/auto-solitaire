import copy
import sys
from definitions import Game, Card, CardType

cache = {}
sys.setrecursionlimit(306385)
#TODO
#no kurwa niezle te ukadanie za pelne stosy
#wyjebywanie rochow z usytego na puste
#kolorki

def move_card(game: Game, move: (int, int, int, bool)) -> Game:
    new_game = copy.deepcopy(game)
    new_game.cards[move[2]].extend(new_game.cards[move[0]][-(move[1]+1):])
    new_game.cards[move[0]] = new_game.cards[move[0]][:-(move[1]+1)]
    new_game.cards[move[2]][-1].is_cheated = move[3]
    return new_game


def get_possible_moves(game: Game) -> list[(int, int, int, bool)]:
    moves = []
    for i, col in enumerate(game.cards):
        if len(col) == 0:
            continue
        if col[-1].is_cheated:
            for des in range(0, 6):
                if des != i and (len(game.cards[des]) == 0 or (
                        game.cards[des][-1].type.value == col[-1].type.value + 1 and not game.cards[des][
                    -1].is_cheated)):
                    moves.insert(0, (i, 0, des, False))
            continue
        last = CardType(col[-1].type.value - 1)
        for d, card in enumerate(reversed(col)):
            if card.type.value != last.value + 1:
                break
            for des in range(0, 6):
                if des != i and ((len(game.cards[des]) == 0 or game.cards[des][0].type != CardType.FULL) or (game.cards[des][0].type != CardType.FULL and not game.cards[des][-1].is_cheated)):
                    if len(game.cards[des]) == 0 or game.cards[des][-1].type.value == card.type.value + 1:
                        moves.insert(0, (i, d, des, False))
                    elif d == 0:
                        moves.append((i, d, des, True))
            last = card.type
    return moves


def is_solved(game: Game) -> bool:
    for col in game.cards:
        if len(col) == 0:
            continue
        last = col[0].type
        if last == CardType.FULL:
            continue
        if last != CardType.T_THING:
            return False
        last = CardType.FULL
        for c in col:
            if c.type.value + 1 != last.value:
                return False
            last = c.type
        if last != game.last_card:
            return False
        col[0].type = CardType.FULL
    return True


def loop(game: Game, bac_moves: list[(int, int, int, bool)]) -> (list[(int, int, int, bool)], bool):
    if hash(game) in cache:
        return [], False
    cache[hash(game)] = True
    if is_solved(game):
        #print(bac_moves)
        print(game)
        return bac_moves, True
    av_moves = get_possible_moves(game)
    if len(av_moves) == 0:
        return [], False
    for move in av_moves:
        huj = loop(move_card(game, move), bac_moves + [move])
        if huj[1]:
            return huj
    return [], False


def solve(game: Game):
    cache.clear()
    print(loop(game, []))


if __name__ == "__main__":
    sample_game = Game()
    #sample_game.add_card(Card(CardType.TEN), 5)
    #sample_game.add_card(Card(CardType.TEN), 5)
    sample_game.add_card(Card(CardType.T_THING), 2)
    sample_game.add_card(Card(CardType.T_THING), 2)
    sample_game.add_card(Card(CardType["QUEEN"]), 4)

    sample_game.add_card(Card(CardType.KING), 1)
    sample_game.add_card(Card(CardType.KING), 1)
    sample_game.add_card(Card(CardType["QUEEN"]), 1)
    sample_game.add_card(Card(CardType.T_THING), 0)
    sample_game.add_card(Card(CardType.KING), 0)
    sample_game.add_card(Card(CardType.QUEEN), 3)
    sample_game.add_card(Card(CardType.JACK), 3)
    sample_game.add_card(Card(CardType.JACK), 5)
    sample_game.add_card(Card(CardType.JACK), 1)
    #sample_game.add_card(Card(CardType.TEN), 2)
    sample_game.add_card(Card(CardType.T_THING), 2)
    sample_game.add_card(Card(CardType.KING), 3)
    sample_game.add_card(Card(CardType.QUEEN), 4)
    sample_game.add_card(Card(CardType.JACK), 5)
    #sample_game.add_card(Card(CardType.TEN), 1)

    sample_game.last_card = CardType.JACK
    print(sample_game, '\n')
    solve(sample_game)
