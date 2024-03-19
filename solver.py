from definitions import Game, Card, CardType

cache = {}


# TODO
def get_possible_moves(game: Game) -> list[(int, int, int, bool)]:
    moves = []
    for i, col in enumerate(game.cards):
        if len(col) == 0:
            continue
        if col[-1].is_cheated:
            for des in range(0, 6):
                if des != i and not game.cards[i][-1].is_cheated and game.cards[i][-2].type.value == col[-1].type.value + 1:
                    moves.append((i, 0, des, False))
            continue
        last = CardType(col[-1].type.value + 1)
        for d, card in enumerate(reversed(col)):
            if card.type.value + 1 != last.value:
                break
            for des in range(0, 6):
                if des != i and (len(game.cards[des]) == 0 or not game.cards[des][-1].is_cheated):
                    if len(game.cards[des]) == 0 or game.cards[des][-1].type.value == card.type.value + 1:
                        moves.insert(0, (i, d, des, False))
                    else:
                        moves.append((i, d, des, True))
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
        return bac_moves, True
    av_moves = get_possible_moves(game)
    print(av_moves)
    if len(av_moves) == 0:
        return [], False
    # TODO
    for move in av_moves:
        pass


def solve(game: Game):
    cache.clear()
    loop(game, [])
    print(is_solved(game))
    print(sample_game)


if __name__ == "__main__":
    sample_game = Game()
    sample_game.add_card(Card(CardType.T_THING), 2)
    sample_game.add_card(Card(CardType.T_THING), 2)
    sample_game.add_card(Card(CardType["QUEEN"]), 2)

    sample_game.add_card(Card(CardType["QUEEN"]), 1)
    sample_game.add_card(Card(CardType.KING), 1)
    sample_game.add_card(Card(CardType.KING), 1)

    sample_game.add_card(Card(CardType.T_THING), 0)
    sample_game.add_card(Card(CardType.KING), 0)
    sample_game.add_card(Card(CardType.QUEEN), 0)
    sample_game.last_card = CardType.QUEEN
    print(sample_game)
    solve(sample_game)
