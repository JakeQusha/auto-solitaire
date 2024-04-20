import copy
import sys
from src.definitions import Game, Card, CardType

cache = {}
sys.setrecursionlimit(306385)


def move_card(game: Game, move: (int, int, int, bool)) -> Game:
    new_game = copy.deepcopy(game)
    new_game.cards[move[2]].extend(new_game.cards[move[0]][-(move[1] + 1):])
    new_game.cards[move[0]] = new_game.cards[move[0]][:-(move[1] + 1)]
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
        if col[0].type == CardType.FULL:
            continue
        last = CardType(col[-1].type.value - 1)
        for d, card in enumerate(reversed(col)):
            if card.type.value != last.value + 1:
                break
            for des in range(0, 6):
                if des != i and ((len(game.cards[des]) == 0) or (
                        game.cards[des][0].type != CardType.FULL and not game.cards[des][-1].is_cheated and
                        game.cards[des][0].type != CardType.FULL)):
                    if len(game.cards[des]) == 0 or game.cards[des][-1].type.value == card.type.value + 1:
                        moves.insert(0, (i, d, des, False))
                    elif d == 0:
                        moves.append((i, d, des, True))
            last = card.type
    return moves


def is_solved(game: Game) -> bool:
    flag = True
    for col in game.cards:
        iflag = False
        if len(col) == 0:
            continue
        last = col[0].type
        if last == CardType.FULL:
            continue
        if last != CardType.T_THING:
            flag = False
            continue
        last = CardType.FULL
        for c in col:
            if c.type.value + 1 != last.value:
                flag = False
                iflag = True
                break
            last = c.type
        if iflag:
            continue
        if last != game.last_card:
            flag = False
            continue
        col[0].type = CardType.FULL
    return flag


def loop(game: Game, bac_moves: list[(int, int, int, bool)]) -> (list[(int, int, int, bool)], bool):
    if game.gethash() in cache:
        return [], False
    cache[game.gethash()] = True
    if is_solved(game):
        # print(bac_moves)
        print(game)
        return bac_moves, True
    av_moves = get_possible_moves(game)
    if len(av_moves) == 0:
        return [], False
    for move in av_moves:
        res = loop(move_card(game, move), bac_moves + [move])
        if res[1]:
            return res
    return [], False


def solve(game: Game) -> (list[(int, int, int, bool)], bool):
    cache.clear()
    return loop(game, [])


if __name__ == "__main__":
    # Test ゲーム
    sample_game = Game()
    sample_game.add_card(Card(CardType.TEN), 5)
    sample_game.add_card(Card(CardType.TEN), 5)
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
    sample_game.add_card(Card(CardType.TEN), 2)
    sample_game.add_card(Card(CardType.T_THING), 2)
    sample_game.add_card(Card(CardType.KING), 5)
    sample_game.add_card(Card(CardType.QUEEN), 4)
    sample_game.add_card(Card(CardType.JACK), 5)
    sample_game.add_card(Card(CardType.TEN), 1)

    sample_game.last_card = CardType.TEN
    print(sample_game, '\n')
    solve(sample_game)
